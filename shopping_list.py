from product import Product
from checkers import QuantityChecker, PriceChecker, StatusChecker


class ShoppingList:
    def __init__(self, name, owner):
        """
        Inicjalizuje obiekt listy zakupów.
        :param name: Nazwa listy zakupów
        :param owner: Właściciel listy zakupów
        :param products: Lista produktów
        :param shared_users: Słownik użytkowników, którzy mają dostęp do listy
        """
        self.name = name
        self.owner = owner
        self._products = []
        self._shared_users = {}

    def add_product(self, product):
        """
        Dodaje produkt do listy zakupów.
        :param product: Produkt do dodania
        """
        if isinstance(product, Product):
            self._products.append(product)
        else:
            raise TypeError("Niewłaściwy typ produktu")
        
    def remove_product(self, name):
        """
        Usuwa produkt z listy zakupów.
        :param product: Produkt do usunięcia
        """
        product = next((p for p in self._products if p.name == name), None)
        if product is None:
            raise ValueError("Produkt nie znajduje się na liście zakupów")
        self._products.remove(product)
        
    def mark_as_bought(self, product):
        """
        Oznacza produkt jako kupiony.
        """
        for p in self._products:
            if p.name == product:
                p.status = "bought"
                return
        raise ValueError("Produkt nie znajduje się na liście zakupów")
        
    def get_products(self):
        """
        Zwraca listę produktów na liście zakupów.
        :return: Lista produktów
        """
        if not self._products:
            raise ValueError("Lista zakupów jest pusta")
        return self._products
    
    def show_list(self):
        """
        Wyświetla listę zakupów.
        """
        if not self._products:
            print("Lista zakupów jest pusta.")
            return
        
        quant_check = QuantityChecker()
        price_check = PriceChecker()
        status_check = StatusChecker()
        print(f"Lista: {self.name}")
        for product in self._products:
            if quant_check.check(product.quantity) and price_check.check(product.price) and \
                status_check.check(product.status, "not bought"):
                print(f"{product.name}, Ilość: {product.quantity}, "
                      f"Cena: {product.price}")
            elif quant_check.check(product.quantity) and price_check.check(product.price) and \
                status_check.check(product.status, "bought"):
                print(f"{product.name}, Ilość: {product.quantity}, "
                      f"Cena: {product.price} - kupiony")
            elif quant_check.check(product.quantity) and status_check.check(product.status, "not bought"):
                print(f"{product.name}, Ilość: {product.quantity}")
            elif quant_check.check(product.quantity) and status_check.check(product.status, "bought"):
                print(f"{product.name}, Ilość: {product.quantity} - kupiony")
            elif status_check.check(product.status, "not bought"):
                print(f"{product.name}")
            elif status_check.check(product.status, "bought"):
                print(f"{product.name} - kupiony")

    def get_total_price(self):
        """
        Zwraca łączną cenę wszystkich produktów na liście zakupów.
        :return: Łączna cena
        """
        total_price = calculate_total_price(self._products)
        if total_price is not None:
            return total_price
        else:
            print("Nie można określić całkowitego kosztu zakupów")
            return None
    
    def share_with_user(self, user, user_manager):
        """
        Udostępnia listę zakupów innemu użytkownikowi.
        :param user: Użytkownik, któremu zostaje udostępniona lista zakupów
        """
        if user_manager.get_user(user) is None:
            raise ValueError("Użytkownik o podanym adresie e-mail nie istnieje")
        if user not in self._shared_users:
            self._shared_users[user] = user_manager.get_user(user)
        else:
            raise ValueError("Lista zakupów jest już udostępniona temu użytkownikowi")
        
def calculate_total_price(products):
    return sum(p.price for p in products if p.price is not None and p.status == "not bought")