use actix_web::{http::header::ContentType, web, App, HttpRequest, HttpResponse, HttpServer};
use serde::{Deserialize, Serialize};
use sqlx::{Connection, PgConnection};

#[derive(Serialize, Deserialize)]
struct Crudie {
    id: u8,
    service_key: String,
    data: u8,
}

async fn create(data: web::Json<Crudie>, connection: web::Data<PgConnection>) -> web::Json<Crudie> {
    let id = sqlx::query!(
        r#"
        INSERT INTO crudie (service_key, data) 
        VALUES ($1, $2) 
        RETURNING id
        "#,
        data.service_key,
        data.data
    )
    .execute(connection.get_ref())
    .await;

    return web::Json(Crudie {
        id: id,
        service_key: data.service_key,
        data: data.data,
    });
}

async fn read(_req: HttpRequest) -> HttpResponse {
    HttpResponse::Ok().finish()
}

async fn update(_req: HttpRequest) -> HttpResponse {
    HttpResponse::Ok().finish()
}

async fn delete(_req: HttpRequest) -> HttpResponse {
    HttpResponse::Ok().finish()
}

#[tokio::main]
async fn main() -> Result<(), std::io::Error> {
    let database_url = std::env::var("DATABASE_URL").expect("no db url");
    let _connection = PgConnection::connect(&database_url)
        .await
        .expect("Failed to connect to db");

    HttpServer::new(|| {
        App::new()
            .route("/create", web::post().to(create))
            .route("/read", web::post().to(read))
            .route("/update", web::post().to(update))
            .route("/delete", web::post().to(delete))
    })
    .bind("127.0.0.1:8000")?
    .run()
    .await
}
