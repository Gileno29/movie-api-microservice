import json
import os
from src.kafka.kafka_consumer import *
from src.models.movie import Movie
from src.database.db import Connection

if __name__ == '__main__':
    consumer= LocalConsumer(os.getenv("TOPIC"),
                                bootstrap_servers=os.getenv("SERVER"),
                                group_id=os.getenv("GROUP"),
                                auto_offset_reset='earliest',
                                enable_auto_commit=True,
                                value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    conection= Connection("api-movies", "userApi", "api", "localhost")
    if conection.ping():
        with conection as con:
            con.execute("CREATE TABLE IF NOT EXISTS movies (id int primary key, name varchar(255), description varchar(255), genre varchar(255), year varchar(255))")
        consumer.consume(conection)
    
    