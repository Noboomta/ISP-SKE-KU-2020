from rental import Rental
from movie import Movie
from PriceCode import PriceCode


class Customer:
    """
       A customer who rents movies.
       The customer object holds information about the
       movies rented for the current billing period,
       and can print a statement of his rentals.
    """
    def __init__(self, name: str):
        """ Initialize a new customer."""
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        if rental not in self.rentals:
            self.rentals.append(rental)

    def get_name(self):
        return self.name

    def statement(self):
        """
            Print all the rentals in current period, 
            along with total charges and reward points.
            Returns:
                the statement as a String
        """
        # total charges
        total_amount = 0
        frequent_renter_points = 0 
        statement = f"Rental Report for {self.name}\n\n"
        fmt = "{:32s}    {:4s} {:6s}\n"
        statement += fmt.format("Movie Title", "Days", "Price")
        fmt = "{:32s}   {:4d} {:6.2f}\n"

        for rental in self.rentals:
            # if rental.get_movie() == PriceCode.NEW_RELEASE:
            #     frequent_renter_points += rental.get_days_rented()
            # else:
            frequent_renter_points += 1
            statement += fmt.format(rental.get_title(), rental.get_days_rented(), rental.cal_amount())
            total_amount += rental.cal_amount()

        statement += "\n"
        statement += "{:32s} {:6s} {:6.2f}\n".format(
                       "Total Charges", "", total_amount)
        statement += "Frequent Renter Points earned: {}\n".format(frequent_renter_points)
        return statement


if __name__ == "__main__":
    customer = Customer("Edward Snowden")
    print(customer.statement())
    movie = Movie("Hacker Noon", Movie.REGULAR)
    customer.add_rental(Rental(movie, 2))
    movie = Movie("CitizenFour", Movie.NEW_RELEASE)
    customer.add_rental(Rental(movie, 3))
    print(customer.statement())
