import json
import os
from src.configs.config import Config
from src.kafka.kafka_consumer import *
from src.kafka.kafka_producer import *
from src.models.movie import Movie
from src.database.db import Connection

if __name__ == '__main__':
    config_producer = Config()
    #config_producer.set_topic(os.getenv("TOPIC_REPLICATION"))

    config_consumer= Config()
    consumer= LocalConsumer(os.getenv("TOPIC"), **config_consumer.get_configs())
    conection= Connection("api-movies", "userApi", "api", "localhost")

    producer=LocalProducer( **config_producer.get_configs_producer() )

    if conection.ping():
        with conection as con:
            con.execute("CREATE TABLE IF NOT EXISTS movies (id int primary key, name varchar(255), description varchar(255), genre varchar(255), year varchar(255))")
        consumer.consume(conection, producer)
    
    