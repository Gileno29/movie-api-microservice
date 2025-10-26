import json
import os
from src.kafka.kafka_consumer import *
from src.models.movie import Movie

if __name__ == '__main__':
    consumer= LocalConsumer(os.getenv("TOPIC"),
                                bootstrap_servers=os.getenv("SERVER"),
                                group_id=os.getenv("GROUP"),
                                auto_offset_reset='earliest',
                                enable_auto_commit=True,
                                value_deserializer=lambda m: json.loads(m.decode('utf-8')))

    consumer.consume()
    
    