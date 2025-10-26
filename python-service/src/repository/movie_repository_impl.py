
from src.repository.movie import MovieInterface
from src.models.movie import Movie


class MovieRepository(MovieInterface):
    def __init__(self, conection):
        self.conection=conection
       
    def create_movie(self, movie) -> Movie:
        with self.conection as con:
            q=f"""INSERT INTO movies(id, name, description,genre, year) \
                VALUES({movie.id},'{movie.name}', '{movie.description}', '{movie.genre}', '{movie.year}')"""
        
            try:
                con.execute(q)
            except Exception as e:
                print(e)
    
