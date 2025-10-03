FROM golang:1.25 AS base

WORKDIR /app

ENV CGO_ENABLED=0
ENV GOPATH=/go
ENV GOCACHE=/go-build

COPY go.mod go.sum ./
RUN go mod download

COPY main.go ./
RUN CGO_ENABLED=0 GOOS=linux go build -o /crudie

EXPOSE 8888

CMD ["/crudie"]
