package main

import (
	"log"
	"os"

	"movie-api/internal/handlers"
	"movie-api/internal/kafka"
	"movie-api/internal/service"

	kafkaClient "github.com/confluentinc/confluent-kafka-go/v2/kafka"
	"github.com/gin-gonic/gin"
)

func main() {
	p, err := kafkaClient.NewProducer(&kafkaClient.ConfigMap{"bootstrap.servers": os.Getenv("SERVER")})
	if err != nil {
		log.Fatalf("Failed to create Kafka producer: %s", err)
	}

	movieProducer := kafka.NewMovieProducer(p, os.Getenv("TOPIC"))
	movieService := service.NewMovieService(movieProducer)
	movieHandler := handlers.NewMovieHandler(movieService)

	r := gin.Default()

	r.POST("/movies", movieHandler.CreateMovie)
	r.PUT("/movies/:id", movieHandler.UpdateMovie)

	if err := r.Run(":8090"); err != nil {
		log.Fatalf("Failed to run server: %s", err)
	}
}
