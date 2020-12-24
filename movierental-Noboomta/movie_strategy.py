class MoviePriceStrategy:
    """Superclass for movie types."""

    def get_price(self, days):
        """Initialize get_price method."""
        return 0


class Regular(MoviePriceStrategy):
    """Regular movie."""

    def get_price(self, days):
        """return price of regular movie"""
        amount = 2.0
        if days > 2:
            amount += 1.5 * (days - 2)
        return amount


class NewRelease(MoviePriceStrategy):
    """New Release Movie."""

    def get_price(self, days):
        """return price of new release movie"""
        amount = 3 * days
        return amount


class Children(MoviePriceStrategy):
    """Children Movie."""

    def get_price(self, days):
        """return price of children movie"""
        amount = 1.5
        if self.days > 3:
            amount += 1.5 * (self.days - 3)
        return amount
