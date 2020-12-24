from pizza_size import PizzaSize


class Pizza:
    """A pizza with a size and optional toppings."""
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'

    def __init__(self, size: PizzaSize):
        if not isinstance(size, PizzaSize):
            raise TypeError('size must be a PizzaSize')
        self.size = size
        self.toppings = []

    def get_price(self):
        """Price of pizza depends on size and number of toppings."""
        if self.size == Pizza.SMALL:
            price = 120 + 20*len(self.toppings)
        elif self.size == Pizza.MEDIUM:
            price = 200 + 25*len(self.toppings)
        elif self.size == Pizza.LARGE:
            price = 280 + 30*len(self.toppings)
        else:
            raise ValueError("Unknown pizza size "+self.size)
        return price

    def add_topping(self, topping):
        """Add a topping to the pizza"""
        if topping not in self.toppings:
            self.toppings.append(topping)

    def describe(self):
        # create printable description of the pizza such as
        # "small pizza with mushroom" or "small plain pizza"
        description = self.size
        if self.toppings:
            description += " pizza with " + ", ".join(self.toppings)
        else:
            description += " plain pizza"
        return description

    def __str__(self):
        # create printable description of the pizza such as
        # "small pizza with mushroom" or "small plain pizza"
        description = self.size
        if self.toppings:
            description += " pizza with " + ", ".join(self.toppings)
        else:
            description += " plain pizza"
        return description
