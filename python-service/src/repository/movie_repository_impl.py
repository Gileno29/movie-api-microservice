
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
                return movie
            except Exception as e:
                print(e)

    def update_movie(self, movie):
        with self.conection as con:
            q=f"""
                UPDATE movies set name='{movie.name}', description='{movie.description}',genre='{movie.genre}', year='{movie.year}'
                """
            try:
                con.execute(q)
                return movie
            except Exception as e:
                    print(e)

            return movie
    
