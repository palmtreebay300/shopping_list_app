import pandas as pd


class Database:
    def __init__(self):
        """
        Inicjalizuje bazę dostępnych produktów.
        :param data: Pusta ramka danych do przechowywania informacji o produktach
        """
        self._data = pd.DataFrame()

    def load_data(self, file_path):
        """
        Ładuje dane o produktach z pliku excel
        :param file_path: Ścieżka do pliku z danymi
        """
        try:
            self._data = pd.read_excel(file_path)
            if 'nazwa' in self._data.columns:
                self._data['nazwa'] = self._data['nazwa'].str.lower()
        except FileNotFoundError:
            print(f"Brak pliku {file_path}.")

    def find_product(self, name):
        """
        Wyszukuje produkt w bazie danych.
        :param name: Nazwa produktu
        :return: Produkt lub None, jeśli nie znaleziono
        """
        name = name.lower()
        if 'nazwa' in self._data.columns:
            product_row = self._data[self._data['nazwa'] == name]
            if not product_row.empty:
                return product_row.iloc[0]
        return None
    
    def get_package_price(self, name):
        """
        Zwraca cenę produktu na podstawie jego nazwy.
        :param name: Nazwa produktu
        :return: Cena produktu lub None, jeśli nie znaleziono
        """
        product = self.find_product(name)
        if product is not None and 'cena za opakowanie' in product:
            return product['cena za opakowanie']
        return None