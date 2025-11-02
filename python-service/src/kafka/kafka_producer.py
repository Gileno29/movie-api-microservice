
import os
#from confluent_kafka import Consumer, KafkaError
from kafka import KafkaProducer
from src.models.movie import Movie
from src.repository.movie_repository_impl import MovieRepository 
import json

class LocalProducer(KafkaProducer):
    def __init__(self, *topics, **configs):
        super().__init__(*topics, **configs)
    
    def produce(self, object):
        self.send('movie-replication', object)