from money import Money

class Check(Money):
    """
    A check with a value and number.
    For this problem we ignore other attributes of a real check.
    >>> c = Check(5000)
    >>> c.value
    5000
    >>> c.check_number
    1000000
    >>> str(c)
    'Check number 1000000 for 5,000.00 Baht'
    >>> m = Money(200)
    >>> str(c+m)           # operators inherited from Money
    '5,200.00 Baht'
    >>> c > m
    True
    >>> c2 = Check(c.value)
    >>> c == c2            # not same because check number is different
    False
    """
    _next_check_number = 1000000

    def __init__(self, amount: float):
        """A new check with a given amount.

        Check number is assigned automatically.
        Arguments:
			amount - value of the check
        """
        super().__init__(amount)
        self.__number = Check._next_check_number
        Check._next_check_number += 1

    @property
    def check_number(self):
        """return the check number"""
        return self.__number
    
    def __eq__(self,other):
        """Two checks are equal if they have same value and check number"""
        if not isinstance(other,Check):
            return False
        return self.check_number == other.check_number and self.value == other.value

    def __str__(self):
        return f"Check number {self.__number:d} for {super().__str__()}"
    
    def __repr__(self):
        return f"Check({self.value})"
