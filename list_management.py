from shopping_list import ShoppingList


class ShoppingListManager:
    def __init__(self):
        """
        Inicjalizuje menedżera listy zakupów.
        :param database: Baza danych produktów
        :param users: Słownik użytkowników
        """
        self.lists = {}

    def create_list(self, name, owner):
        """
        Tworzy nową listę zakupów.
        :param name: Nazwa listy zakupów
        :param owner: Właściciel listy zakupów
        :return: Obiekt ShoppingList
        """
        if name not in self.lists:
            shopping_list = ShoppingList(name, owner)
            self.lists[name] = shopping_list
            return shopping_list
        else:
            raise ValueError("Lista o podanej nazwie już istnieje")
        
    def remove_list(self, name, owner):
        """
        Usuwa listę zakupów.
        :param name: Nazwa listy zakupów
        :param owner: Właściciel listy zakupów
        """
        if name in self.lists and self.lists[name].owner == owner:
            del self.lists[name]
        else:
            raise ValueError("Lista o podanej nazwie nie istnieje lub nie jest własnością tego użytkownika")
        
    def show_lists(self, lists):
        """
        Wyświetla listę zakupów.
        :param lists: Lista zakupów
        """
        if not lists:
            print("Brak list zakupów.")
            return
        for name in lists:
            print(name)