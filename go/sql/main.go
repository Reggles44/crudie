package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/jackc/pgx/v5/pgxpool"
)

var (
	dbPool *pgxpool.Pool
	err    error
)

type Crudie struct {
	ID         uint   `json:"id"`
	ServiceKey string `json:"service_key"`
	Data       int    `json:"data"`
}

func createHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	var data Crudie
	err := json.NewDecoder(r.Body).Decode(&data)
	if err != nil {
		http.Error(w, "", http.StatusBadRequest)
		return
	}

	log.Printf("CREATE %+v", data)

	insertSql := `INSERT INTO crudie (service_key, data) VALUES ($1, $2) RETURNING id`
	err = dbPool.QueryRow(context.Background(), insertSql, data.ServiceKey, data.Data).Scan(&data.ID)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusAccepted)
	json.NewEncoder(w).Encode(data)
}

func readHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	serviceKey := r.URL.Query().Get("service_key")
	if serviceKey == "" {
		http.Error(w, "", http.StatusBadRequest)
		return
	}
	log.Printf("READ service_key=" + serviceKey)

	var data Crudie
	readSql := `SELECT id, service_key, data FROM crudie WHERE service_key = $1`
	err = dbPool.QueryRow(context.Background(), readSql, serviceKey).Scan(&data.ID, &data.ServiceKey, &data.Data)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusAccepted)
	json.NewEncoder(w).Encode(data)

}

func updateHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	var data Crudie
	err := json.NewDecoder(r.Body).Decode(&data)
	if err != nil {
		http.Error(w, "", http.StatusBadRequest)
		return
	}

	log.Printf("UPDATE %+v", data)

	updateSql := `UPDATE crudie SET data = $2 WHERE service_key = $1 RETURNING id`
	err = dbPool.QueryRow(context.Background(), updateSql, data.ServiceKey, data.Data).Scan(&data.ID)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusAccepted)
	json.NewEncoder(w).Encode(data)

}

func deleteHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	serviceKey := r.URL.Query().Get("service_key")
	if serviceKey == "" {
		http.Error(w, "", http.StatusBadRequest)
		return
	}
	log.Printf("DELETE service_key=" + serviceKey)

	var data Crudie
	deleteSql := `DELETE FROM crudie WHERE service_key = $1 RETURNING id, service_key, data`
	err = dbPool.QueryRow(context.Background(), deleteSql, serviceKey).Scan(&data.ID, &data.ServiceKey, &data.Data)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusAccepted)
	json.NewEncoder(w).Encode(data)

}

func main() {
	port := os.Getenv("PORT")
	if port == "" {
		log.Panic("$PORT must be set")
	}

	dbPool, err = pgxpool.New(context.Background(), os.Getenv("DATABASE_URL"))
	if err != nil {
		log.Panic("failed to connect database")
	}
	if dbPool.Ping(context.Background()) != nil {
		log.Panic("failed to connect database")
	}
	defer dbPool.Close()

	http.HandleFunc("POST /create", createHandler)
	http.HandleFunc("GET /read", readHandler)
	http.HandleFunc("PUT /update", updateHandler)
	http.HandleFunc("DELETE /delete", deleteHandler)

	// Start the server
	log.Println(fmt.Sprintf("Starting Server on port %s", port))
	log.Fatal(http.ListenAndServe(fmt.Sprintf(":%v", port), nil))
}
