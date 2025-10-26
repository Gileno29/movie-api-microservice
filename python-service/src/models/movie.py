class Movie():
    def __init__(self, id, name, description, genre, year):
        self.id=id
        self.name=name
        self.description=description
        self.genre=genre
        self.year= year
    
    def __str__(self) -> str:
        obj= f'{self.description}, {self.id}, {self.name}'
        return obj