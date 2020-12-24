from datetime import date, time
from django.db import models
import datetime
from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator

class Sale(models.Model):
    datetime = timezone.now
    line_items = []
    tax = 0
    def addItem(self, product, quantity):
        self.line_items.append(LineItem(product, quantity))
    def getTotal(self):
        return self.LineItem
    def getTax(self):
        return self.tax

class LineItem(models.Model):
    def __init__(self, product, quantity):
        self.quantity = quantity
        self.product = Product(1, " ", 30)
    def getPrice(self):
        return self.quantity * self.product.unit_price

class Product(models.Model):
    def __init__(self, product_code, description, unit_price):
        self.product_code = product_code
        self.description = description
        self.unit_price = unit_price
