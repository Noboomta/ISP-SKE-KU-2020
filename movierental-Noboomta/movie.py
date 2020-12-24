# from PriceCode import PriceCode


class Movie:
	"""
	A movie available for rent.
	"""

	def __init__(self, title,  year, genre):
		"""Initialize a new movie."""
		self.title = title
		self.year = year
		self.genre = genre

	def get_genre(self):
		return self.genre

	def is_genre(self, genre):
		return genre in self.genre

	def get_year(self):
		return self.year

	def get_title(self):
		return self.title

	def __str__(self):
		return self.title
