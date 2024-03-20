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

async fn create(data: web::Json<Crudie>, connection: web::Data<PgPool>) -> HttpResponse {
    let mut new_data = data.into_inner();
    new_data.id = Some(
        sqlx::query!(
            r#"
        INSERT INTO crudie (service_key, data) 
        VALUES ($1, $2) 
        RETURNING id
        "#,
            new_data.service_key,
            new_data.data,
        )
        .fetch_one(connection.get_ref())
        .await
        .expect("failed to insert into db")
        .id,
    );

    HttpResponse::Ok().json(new_data)
}

async fn read(data: web::Query<Crudie>, connection: web::Data<PgPool>) -> HttpResponse {
    let result:  = sqlx::query!(
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

    if result

    HttpResponse::Ok().finish()
}

async fn update(req: HttpRequest) -> HttpResponse {
    HttpResponse::Ok().finish()
}

async fn delete(req: HttpRequest) -> HttpResponse {
    HttpResponse::Ok().finish()
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
            .route("/read", web::post().to(read))
            .route("/update", web::post().to(update))
            .route("/delete", web::post().to(delete))
            .app_data(connection.clone())
    })
    .bind("0.0.0.0:8000")?
    .run()
    .await
}
