use actix_web::{web, App, HttpRequest, HttpResponse, HttpServer};

async fn create(_req: HttpRequest) -> HttpResponse {
    HttpResponse::Ok().finish()
}

#[tokio::main]
async fn main() -> Result<(), std::io::Error> {
    println!("HELLO WORLD");
    HttpServer::new(|| App::new().route("/create", web::post().to(create)))
        .bind("127.0.0.1:8000")?
        .run()
        .await
}
