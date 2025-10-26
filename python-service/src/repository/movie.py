from abc import ABC, abstractmethod
from src.models.movie import Movie
class MovieInterface(ABC):
    @abstractmethod
    def create_movie(self, movie) -> Movie:
        """Saves the movie data and returns the movie object."""
        pass
    def update_movie(self,movie) -> Movie:
        """Updates the movie data and returns the movie object."""
        pass

    def delete_movie(self, id)-> str:
        """Delete the movie and returns a message."""
        pass
