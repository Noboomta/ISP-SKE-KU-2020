from movie import Movie
import csv
from datetime import datetime

class MovieCatalog:

    def __init__(self) -> None:
        self.movie = []

    def read(self, filename='moviedata.csv'):
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            self.movie = list(reader)

    def get_movie(self, title):
        self.read()
        for movie in self.movie:
            if(movie[1] == title):
                return Movie(title, int(movie[2]), movie[3].split("|"))

        return "No movie"