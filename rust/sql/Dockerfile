FROM rust:1.76 as base

WORKDIR /app
COPY Cargo.toml Cargo.lock ./
COPY /src ./src
COPY .sqlx ./.sqlx

FROM base as develop

RUN cargo build --release

EXPOSE 8000
CMD ["./target/release/crudie"]
