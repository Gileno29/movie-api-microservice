# Movie API Kafka

## Overview

This project is a Go-based microservice that exposes a simple API for creating and updating movies. It uses Apache Kafka to produce messages for movie creation and update events. The service is built with Gin for handling HTTP requests and confluent-kafka-go for Kafka integration.

## Features

*   Create a new movie
*   Update an existing movie
*   Produces Kafka messages for movie creation and updates

## Technologies Used

*   [Go](https://golang.org/)
*   [Gin](https://github.com/gin-gonic/gin)
*   [Apache Kafka](https://kafka.apache.org/)
*   [Docker](https://www.docker.com/)
*   [Docker Compose](https://docs.docker.com/compose/)
*   [confluent-kafka-go](https://github.com/confluentinc/confluent-kafka-go)

## Getting Started

### Prerequisites

*   [Docker](https://docs.docker.com/get-docker/)
*   [Docker Compose](https://docs.docker.com/compose/install/)
*   [Go](https://golang.org/doc/install) (1.23.0 or later)

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/your-username/movie-api-kafka.git
    cd movie-api-kafka/go-service
    ```

2.  Create a `.env` file in the `go-service` directory with the following content:

    ```
    SERVER=localhost:9092
    TOPIC=movies
    ```

### Running the Application

1.  Start the Kafka cluster and Kafka UI using Docker Compose:

    ```bash
    docker-compose up -d
    ```

2.  Run the Go application:

    ```bash
    go run cmd/main.go
    ```

The API will be running at `http://localhost:8090`.

## API Endpoints

### Create Movie

*   **URL:** `/movies`
*   **Method:** `POST`
*   **Body:**

    ```json
    {
      "id": "a-uuid",
      "name": "The Godfather",
      "description": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
      "genre": "Crime, Drama",
      "year": 1972
    }
    ```

*   **Success Response:**

    *   **Code:** 201 Created
    *   **Content:**

        ```json
        {
          "id": "a-uuid",
          "name": "The Godfather",
          "description": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
          "genre": "Crime, Drama",
          "year": 1972
        }
        ```

### Update Movie

*   **URL:** `/movies/:id`
*   **Method:** `PUT`
*   **Body:**

    ```json
    {
      "id": "a-uuid",
      "name": "The Godfather",
      "description": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
      "genre": "Crime, Drama",
      "year": 1972
    }
    ```

*   **Success Response:**

    *   **Code:** 201 Created
    *   **Content:**

        ```json
        {
          "id": "a-uuid",
          "name": "The Godfather",
          "description": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
          "genre": "Crime, Drama",
          "year": 1972
        }
        ```

## Environment Variables

*   `SERVER`: The address of the Kafka bootstrap server (e.g., `localhost:9092`).
*   `TOPIC`: The Kafka topic to which movie events are produced (e.g., `movies`).
