
import os
#from confluent_kafka import Consumer, KafkaError
from kafka import KafkaConsumer
from src.models.movie import Movie
from src.repository.movie_repository_impl import MovieRepository 
import json

class LocalConsumer(KafkaConsumer):
         
    def consume(self, c):
        repository= MovieRepository(c)
        print(f"[*] Consumidor Kafka iniciado no tópico:{os.getenv("TOPIC")}")

        try:
            while True:
                for msg in self:              
                    if msg is None:
                        continue
                    try:

                        movie_data = json.loads(json.dumps(msg.value))
                        

                        # 2. Lógica de Persistência no DB
                    # save_to_database(movie_data) 
                        movie= Movie(movie_data['Value']['id'],
                                      movie_data['Value']['description'],
                                      movie_data['Value']['name'],
                                      movie_data['Value']['genre'],
                                      movie_data['Value']['year'])
                        print(f"Receivet movie: {movie_data}")

                        if movie_data['Type']=='Movie.Created':
                            print("Trying to create a movie")
                            repository.create_movie(movie)

                        if movie_data['Type']=='Movie.Updated':
                            print("Trying to update a movie")
                            repository.update_movie(movie)

                    except Exception as e:
                        print(f"Erro ao processar mensagem: {e}")
                    

        except KeyboardInterrupt:
            pass
        finally:
          
            self.close()
            print("\nConsumidor encerrado.")


    def save_to_database(book_data):
        """
        Simulação da lógica para salvar no banco de dados.
        Aqui é onde você usaria seu driver DB ou ORM (SQLAlchemy).
    """
    
    # Exemplo: Usando SQL puro (apenas um esboço)
    # conn = engine.connect()
    # conn.execute(
    #    "INSERT INTO books (title, author, isbn) VALUES (%s, %s, %s)",
    #    (book_data['title'], book_data['author'], book_data['isbn'])
    # )
    # conn.close()
    
        print(f"   -> Livro '{book_data.get('title')}' salvo no DB (simulado).")