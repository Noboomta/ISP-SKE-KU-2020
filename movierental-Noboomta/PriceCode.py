from datetime import datetime
from enum import Enum
from movie import Movie
from datetime import datetime

class PriceCode(Enum):
    NEW_REALEASE = {"price": lambda days: 3 * days,
                    "frequent_rental_points": lambda days: days
                    }
    REGULAR = {"price": lambda days: (1.5 * days) + 2.0 if (days > 2) else 2,
                "frequent_rental_points": lambda days: 1
                }
    CHILDREN = {"price": lambda days: (1.5 * days) + 2.5 if (days > 3) else 1.5,
                "frequent_rental_points": lambda days: 1
                }

    def frequent_rental_points(self, day):
        frequent_rental_point = self.value["frequent_rental_points"]
        return frequent_rental_point(day)

    def price(self, day: int):
        price_here = self.value["price"]
        return price_here(day)

    @classmethod
    def for_movie(cls, movies: Movie):
        price_code = PriceCode.REGULAR
        # if("Children" in str(movies.get_genre())):
        if int(movies.get_year()) == datetime.now().year:
            price_code = PriceCode.NEW_REALEASE
        elif movies.is_genre("Children"):
            price_code = PriceCode.CHILDREN
        return price_code