# Movie API with Kafka

This project is a demonstration of a microservices architecture using Go and Python, with Kafka as a message broker.

## Running the project

To run the project, you can use the `compose.yml` file in the `go-service` directory.

```bash
cd go-service
docker-compose up -d
```

## Project Structure

The project is divided into two services:

- **go-service**: A Go service that exposes a REST API to create, and list movies. It also produces messages to a Kafka topic when a new movie is created.
- **python-service**: A Python service that consumes messages from the Kafka topic and saves the movie to a database.
