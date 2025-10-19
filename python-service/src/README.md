# Movie API Kafka

## Description

This project is a Python-based microservice that listens to a Kafka topic for messages about new movies. When a message is received, it's processed and saved to a PostgreSQL database.

## Features

- Consumes messages from a Kafka topic.
- Saves movie data to a PostgreSQL database.
- Uses the repository pattern to separate data access logic from business logic.

## Technologies Used

- Python
- Kafka (`confluent_kafka`)
- PostgreSQL (`psycopg2`)

## Project Structure

```
/home/gileno/Documentos/Projetos/movie_api_kafka/python-service/src/
├───database/
│   └───db.py
├───kafka/
│   └───kafka-consumer.py
├───models/
│   ├───__init__.py
│   └───movie.py
└───repository/
    ├───__init__.py
    ├───movie_repository_impl.py
    └───movie.py
```

## How to Run

1. **Clone the repository:**

```bash
git clone https://github.com/gilenofilho/movie_api_kafka.git
```

2. **Install the dependencies:**

```bash
pip install -r requirements.txt
```

3. **Set the environment variables:**

```bash
export SERVER=<your_kafka_server>
export GROUP=<your_kafka_group>
export OFFSET=<your_kafka_offset>
export TOPIC=<your_kafka_topic>
```

4. **Run the application:**

```bash
python main.py
```

## Environment Variables

- `SERVER`: The address of your Kafka server.
- `GROUP`: The ID of your consumer group.
- `OFFSET`: The offset to start consuming from.
e `TOPIC`: The topic to consume from.
