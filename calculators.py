import pandas as pd
from math import ceil
from product import Drink, Food

# quant_calc = QuantityCalculator([], [])


class QuantityCalculator:
    def __init__(self, shopping_list, database):
        self.shopping_list = shopping_list
        self.database = database

    def calculate_quantity(self):
      for product in self.shopping_list._products:
        if product.quantity is not None:
          continue
        searched_product = self.database.find_product(product.name)
        if searched_product.empty:
          continue

        if isinstance(product, Drink):
            package_volume = searched_product.get('objętość opakowania [ml]')
            if product.volume and pd.notna(package_volume) and package_volume > 0:
                product.quantity = ceil(product.volume / package_volume)

        elif isinstance(product, Food):
            package_weight = searched_product.get('masa produktu [g]')
            if product.weight and pd.notna(package_weight) and package_weight > 0:
                product.quantity = ceil(product.weight / package_weight)


class PriceCalculator:
    def __init__(self, shopping_list, database):
        self.shopping_list = shopping_list
        self.database = database

    def calculate_price(self):
        for product in self.shopping_list._products:
            if product.price is not None:
                continue
            package_price = self.database.get_package_price(product.name)
            if package_price is not None and product.quantity is not None:
                    product.price = package_price * product.quantity