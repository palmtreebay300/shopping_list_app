class Person:
    def __init__(self, name, email):
        """
        Inicjalizuje obiekt osoby.
        :param name: Imię
        :param email: Adres e-mail
        :param owned_lists: Słownik list zakupowych należących do osoby
        :param shared_lists: Słownik udostępnionych osobie list zakupowych
        """
        self.name = name
        self.email = email.lower()
        self.owned_lists = {}
        self.shared_lists = {}


class UserManager:
    def __init__(self):
        """
        Inicjalizuje menedżera użytkowników.
        :param users: Słownik użytkowników
        """
        self.users = {}

    def add_user(self, name, email):
        """
        Dodaje nowego użytkownika do systemu.
        :param name: Imię użytkownika
        :param email: Adres e-mail użytkownika
        """
        if email.lower() not in self.users:
            self.users[email.lower()] = Person(name, email)
            print(self.users)
        else:
            raise ValueError("Użytkownik o podanym adresie e-mail już istnieje")

    def get_user(self, email):
        """
        Zwraca obiekt użytkownika na podstawie adresu e-mail.
        :param email: Adres e-mail użytkownika
        :return: Obiekt użytkownika lub None, jeśli nie znaleziono
        """
        return self.users.get(email.lower(), None)
    

class LoginManager:
    def __init__(self, user_manager):
        """
        Inicjalizuje menedżera logowania.
        :param user_manager: Menedżer użytkowników
        """
        self.user_manager = user_manager

    def login(self, email):
        """
        Loguje użytkownika na podstawie adresu e-mail.
        :param email: Adres e-mail użytkownika
        :return: Obiekt użytkownika lub None, jeśli nie znaleziono
        """
        user = self.user_manager.get_user(email)
        if user is None:
            raise ValueError("Użytkownik o podanym adresie e-mail nie istnieje")
        return user

    def register(self, name, email):
        """
        Rejestruje nowego użytkownika.
        :param name: Imię użytkownika
        :param email: Adres e-mail użytkownika
        """
        self.user_manager.add_user(name, email)