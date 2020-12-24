from PriceCode import PriceCode

class Rental:
	"""
	A rental of a movie by customer.
	From Fowler's refactoring example.

	A realistic Rental would have fields for the dates
	that the movie was rented and returned, from which the
	rental period is calculated.
	But for simplicity of the example only a days_rented
	field is used.
	"""

	def __init__(self, movie, days_rented): 
		"""Initialize a new movie rental object for
			a movie with known rental period (daysRented).
		"""
		self.price_code = PriceCode.for_movie(movie)
		self.movie = movie
		self.days_rented = days_rented

	def get_title(self):
		return self.movie.get_title()

	def get_days_rented(self):
		return self.days_rented
	

	def cal_amount(self):
		amount = self.price_code.price(self.days_rented)
		return amount

	def get_frequent(self):
		"""Return frequency of movie rent."""
		return self.price_code.frequent_rental_points(self.days_rented)
