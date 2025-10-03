package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/go-playground/validator/v10"
	"gorm.io/gorm"
	"gorm.io/driver/postgres"
)

type FooBar struct {
	ID  uint   `json:"id" db:"id"`
	Foo string `json:"foo" db:"foo" validate:"required"`
	Bar int    `json:"bar" db:"bar" validate:"required"`
}

func (foobar *FooBar) TableName() string {
	return "foobar"
}

func main() {
	port := os.Getenv("PORT")
	if port == "" {
		port = "8888"
	}

	dbURL := os.Getenv("DATABASE_URL")
	if dbURL == "" {
		log.Fatal("Missing DATABASE_URL")
	}
	db, err := gorm.Open(postgres.Open(dbURL), &gorm.Config{})
	if err != nil {
		log.Fatal("Database Connection failed", err)
	}

	foobarValidator := validator.New(validator.WithRequiredStructEnabled())

	http.HandleFunc("GET /", func(w http.ResponseWriter, r *http.Request) {
		log.Printf("--> %s %s", r.Method, r.URL.Path)
		w.WriteHeader(http.StatusOK)
	})

	http.HandleFunc("POST /create", func(w http.ResponseWriter, r *http.Request) {
		log.Printf("--> %s %s", r.Method, r.URL.Path)

		var foobar FooBar
		err := json.NewDecoder(r.Body).Decode(&foobar)
		if err != nil {
			w.WriteHeader(http.StatusBadRequest)
			return
		}

		err = foobarValidator.Struct(foobar)
		if err != nil {
			w.WriteHeader(http.StatusBadRequest)
			return
		}

		result := db.Create(&foobar)
		if result.Error != nil {
			w.WriteHeader(http.StatusBadRequest)
			return
		}

		responseData, err := json.Marshal(foobar)
		if err != nil {
			w.WriteHeader(http.StatusBadRequest)
			return
		}

		w.Write(responseData)
		w.WriteHeader(http.StatusOK)
	})

	http.HandleFunc("GET /read/{id}", func(w http.ResponseWriter, r *http.Request) {
		log.Printf("--> %s %s", r.Method, r.URL.Path)

		id := r.PathValue("id")
		var foobar FooBar
		db.Find(&foobar, id)

		responseData, err := json.Marshal(foobar)
		if err != nil {
			w.WriteHeader(http.StatusBadRequest)
			return
		}

		w.Write(responseData)
		w.WriteHeader(http.StatusOK)
	})

	http.HandleFunc("PATCH /update/{id}", func(w http.ResponseWriter, r *http.Request) {
		log.Printf("--> %s %s", r.Method, r.URL.Path)

		id := r.PathValue("id")
		var foobarUpdate FooBar

		err := json.NewDecoder(r.Body).Decode(&foobarUpdate)
		if err != nil {
			w.WriteHeader(http.StatusBadRequest)
			return
		}

		err = foobarValidator.Struct(foobarUpdate)
		if err != nil {
			w.WriteHeader(http.StatusBadRequest)
			return
		}

		var foobar FooBar
		db.Find(&foobar, id)

		if foobarUpdate.Foo != "" {
			foobar.Foo = foobarUpdate.Foo
		}

		if foobarUpdate.Bar != 0 {
			foobar.Bar = foobarUpdate.Bar
		}

		responseData, err := json.Marshal(foobar)
		if err != nil {
			w.WriteHeader(http.StatusBadRequest)
			return
		}

		w.Write(responseData)
		w.WriteHeader(http.StatusOK)
	})

	http.HandleFunc("DELETE /delete/{id}", func(w http.ResponseWriter, r *http.Request) {
		log.Printf("--> %s %s", r.Method, r.URL.Path)

		id := r.PathValue("id")
		var foobar FooBar
		db.Find(&foobar, id)
		db.Delete(&foobar)

		responseData, err := json.Marshal(foobar)
		if err != nil {
			w.WriteHeader(http.StatusBadRequest)
			return
		}

		w.Write(responseData)
		w.WriteHeader(http.StatusOK)
	})

	// Start the server
	log.Println(fmt.Sprintf("Starting Server on port %s", port))
	log.Fatal(http.ListenAndServe(fmt.Sprintf(":%v", port), nil))
}
