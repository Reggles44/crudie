FROM golang:1.22 as base

WORKDIR /app

ENV CGO_ENABLED 0
ENV GOPATH /go
ENV GOCACHE /go-build

COPY go.mod go.sum ./
RUN go mod download
COPY *.go ./

###

FROM base as develop

RUN CGO_ENABLED=0 GOOS=linux go build -o /crudie

EXPOSE 8080

CMD ["/crudie"]
