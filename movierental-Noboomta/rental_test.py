import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):

	def setUp(self):
		self.new_movie = Movie("Mulan", Movie.NEW_RELEASE)
		self.regular_movie = Movie("CitizenFour", Movie.REGULAR)
		self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie."""
		m = Movie("CitizenFour", Movie.REGULAR)
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(Movie.REGULAR, m.get_price_code())

	def test_rental_price(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.cal_amount(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.cal_amount(), 15.0)
		rental = Rental(self.regular_movie, 3)
		self.assertEqual(rental.cal_amount(), 3.5)
		rental = Rental(self.childrens_movie, 2)
		self.assertEqual(rental.cal_amount(), 1.5)

	def test_rental_points(self):
		"""test if the frequent is correct."""
		rental = Rental(self.new_movie, 3.0)
		self.assertEqual(rental.get_frequent(), 3.0)
		rental = Rental(self.regular_movie, 3.0)
		self.assertEqual(rental.get_frequent(), 1)
		rental = Rental(self.childrens_movie, 3.0)
		self.assertEqual(rental.get_frequent(), 1)
