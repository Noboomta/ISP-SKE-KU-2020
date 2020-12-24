# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from MovieCatalog import MovieCatalog
from movie import Movie
from rental import Rental
from customer import Customer
from PriceCode import PriceCode

def make_movies():
    movie_catalog = MovieCatalog()
    movies = [
        # Movie("The Irishman", PriceCode.NEW_REALEASE, "story"),
        # Movie("CitizenFour", PriceCode.REGULAR, "story"),
        # # Movie("Frozen", Movie.CHILDRENS),
        # Movie("El Camino", Movie.NEW_RELEASE),
        # Movie("Particle Fever", Movie.REGULAR)
        movie_catalog.get_movie("Mulan"),
        movie_catalog.get_movie("Hacksaw Ridge")
    ]
    return movies

if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())

    # movieCatalog = MovieCatalog()
    # movieCatalog.read()
    # arrival = movieCatalog.get_movie("Arrival")
    # print(arrival.title, arrival.get_year(), arrival.get_price_code(), arrival.get_genre())

    # catalog = MovieCatalog()
    # catalog.read()
    # movie = catalog.get_movie("Mulan")
    # price_code = PriceCode.for_movie(movie)
    # print(price_code)
