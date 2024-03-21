use actix_web::{middleware::Logger, web, App, HttpRequest, HttpResponse, HttpServer};
use env_logger::Env;
use serde::{Deserialize, Serialize};
use sqlx::PgPool;

#[derive(Serialize, Deserialize)]
struct Crudie {
    id: Option<i32>,
    service_key: String,
    data: Option<i32>,
}

async fn create(
    data: web::Json<Crudie>,
    _req: HttpRequest,
    connection: web::Data<PgPool>,
) -> HttpResponse {
    let id = Some(
        sqlx::query!(
            r#"
            INSERT INTO crudie (service_key, data) 
            VALUES ($1, $2) 
            RETURNING id
            "#,
            data.service_key,
            data.data,
        )
        .fetch_one(connection.get_ref())
        .await
        .expect("failed to insert into db")
        .id,
    );

    HttpResponse::Ok().json(Crudie {
        id,
        service_key: data.service_key.to_string(),
        data: data.data,
    })
}

async fn read(
    data: web::Query<Crudie>,
    _req: HttpRequest,
    connection: web::Data<PgPool>,
) -> HttpResponse {
    let result = sqlx::query!(
        r#"
        SELECT id, service_key, data
        FROM crudie
        WHERE service_key = $1
        LIMIT 1
        "#,
        data.service_key,
    )
    .fetch_one(connection.get_ref())
    .await
    .expect("failed to select from db");

    HttpResponse::Ok().json(Crudie {
        id: Some(result.id),
        service_key: result.service_key.expect("no service_key for result"),
        data: result.data,
    })
}

async fn update(
    data: web::Json<Crudie>,
    _req: HttpRequest,
    connection: web::Data<PgPool>,
) -> HttpResponse {
    let id: Option<i32> = Some(
        sqlx::query!(
            r#"
            UPDATE crudie
            SET data = $1
            WHERE service_key = $2
            RETURNING id
            "#,
            data.data,
            data.service_key
        )
        .fetch_one(connection.get_ref())
        .await
        .expect("failed to update record in db")
        .id,
    );

    HttpResponse::Ok().json(Crudie {
        id,
        service_key: data.service_key.to_string(),
        data: data.data,
    })
}

async fn delete(
    data: web::Query<Crudie>,
    _req: HttpRequest,
    connection: web::Data<PgPool>,
) -> HttpResponse {
    let id: Option<i32> = Some(
        sqlx::query!(
            r#"
            DELETE FROM crudie
            WHERE service_key = $1
            RETURNING id
            "#,
            data.service_key,
        )
        .fetch_one(connection.get_ref())
        .await
        .expect("failed to delete record from db")
        .id,
    );

    HttpResponse::Ok().json(Crudie {
        id,
        service_key: data.service_key.to_string(),
        data: data.data,
    })
}

#[tokio::main]
async fn main() -> Result<(), std::io::Error> {
    env_logger::Builder::from_env(Env::default().default_filter_or("info")).init();
    log::info!("Starting...");

    let database_url = std::env::var("DATABASE_URL").expect("no db url");
    let pg_pool = PgPool::connect(&database_url)
        .await
        .expect("failed to connect to db");
    let connection = web::Data::new(pg_pool);

    log::info!("Attached to 0.0.0.0:8000");
    HttpServer::new(move || {
        App::new()
            .wrap(Logger::default())
            .route("/create", web::post().to(create))
            .route("/read", web::get().to(read))
            .route("/update", web::put().to(update))
            .route("/delete", web::delete().to(delete))
            .app_data(connection.clone())
    })
    .bind("0.0.0.0:8000")?
    .run()
    .await
}
