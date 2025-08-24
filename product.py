class Product:
    def __init__(self, name):
        """
        Inicjalizuje obiekt produktu.
        :param name: Nazwa produktu
        :param quantity: Ilość produktu
        :param price: Cena produktu
        :param status: Status produktu (nie kupiony, kupiony)
        """
        self.name = name.lower()
        self.quantity = None
        self.price = None
        self.status = "not bought"


class Drink(Product):
    def __init__(self, name, quantity=None, volume=None):
        """
        Inicjalizuje obiekt napoju.
        :param name: Nazwa
        :param quantity: Ilość (liczba butelek lub puszek)
        :param volume: Objętość (ml)
        """
        super().__init__(name)
        self.quantity = quantity
        self.volume = volume


class Food(Product):
    def __init__(self, name, quantity=None, weight=None):
        """
        Inicjalizuje obiekt produktu spożywczego.
        :param name: Nazwa
        :param quantity: Ilość (liczba sztuk)
        :param weight: Waga (g)
        """
        super().__init__(name)
        self.quantity = quantity
        self.weight = weight
