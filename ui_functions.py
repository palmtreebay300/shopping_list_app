from product import Product, Drink, Food
from data_management import Database
from calculators import QuantityCalculator, PriceCalculator


def choose_option(opt_numbers):
    """
    Funkcja do wyboru opcji z listy.
    :param options: Ilość dostępnych opcji
    :return: Numer wybranej opcji
    """
    while True:
        try:
            choice = int(input("Wybierz opcję: "))
            if choice in range(1, opt_numbers+1):
                return choice
            else:
                print("Nieprawidłowa wartość.")
        except ValueError:
            print("Proszę wprowadzić liczbę.")

def login_page():
    print("1. Logowanie")
    print("2. Rejestracja")
    print("3. Wyjście")

def process_login_page(option, login_manager):
    if option == 1:
        email = input("Podaj adres e-mail: ")
        user = login_manager.login(email)
        return user
    elif option == 2:
        name = input("Podaj swoje imię: ")
        email = input("Podaj adres e-mail: ")
        login_manager.register(name, email)
        print("Rejestracja zakończona pomyślnie.")
        return login_manager.login(email)
    elif option == 3:
        print("Wyjście z programu.")
        exit()

def user_page(user):
    print(f"Zalogowano jako {user.name}, {user.email}")
    print("1. Utwórz Listę zakupów")
    print("2. Usuń Listę Zakupów")
    print("3. Pokaż Własne Listy")
    print("4. Pokaż Udostepnione Listy")
    print("5. Wybierz Listę")
    print("6. Wyloguj")
    print("7. Wyjście")

def process_user_page(user, option, list_manager):
    while True:
        user_page(user)
        option = choose_option(7)
        if option == 1:
            list_name = input("Podaj nazwę listy zakupów: ")
            shopping_list = list_manager.create_list(list_name, user)
            user.owned_lists[list_name] = shopping_list
            print(f"Lista zakupów '{list_name}' została utworzona.")
            return shopping_list
        elif option == 2:
            if not user.owned_lists:
                print("Brak list zakupów do usunięcia.")
                continue
            list_manager.show_lists(user.owned_lists.keys())
            list_name = input("Podaj nazwę listy zakupów do usunięcia: ")
            if list_name in user.owned_lists:
                list_manager.remove_list(list_name, user)
                del user.owned_lists[list_name]
                print(f"Lista zakupów '{list_name}' została usunięta.")
            else:
                print("Brak listy o podanej nazwie.")
            return None
        elif option == 3:
            print("Twoje listy zakupów:")
            list_manager.show_lists(user.owned_lists.keys())
            return None
        elif option == 4:
            print("Udostępnione listy zakupów:")
            list_manager.show_lists(user.shared_lists.keys())
            return None
        elif option == 5:
            if not user.owned_lists and not user.shared_lists:
                print("Brak list zakupów do wyboru.")
                continue
            merged_lists = {**user.owned_lists, **user.shared_lists}
            list_manager.show_lists(merged_lists.keys())
            list_name = input("Podaj nazwę listy zakupów do wyboru: ")
            if list_name in user.owned_lists:
                list = user.owned_lists[list_name]
            elif list_name in user.shared_lists:
                list = user.shared_lists[list_name]
            else:
                print("Lista zakupów nie istnieje.")
                continue
            print(f"Wybrano listę zakupów: {list_name}")
            return list
        elif option == 6:
            return None
        elif option == 7:
            exit()

def menu_page():
    print("1. Dodaj Produkt")
    print("2. Usuń Produkt")
    print("3. Oznacz Produkt Jako Kupiony")
    print("4. Wyświetl Listę")
    print("5. Całkowity Koszt Zakupów")
    print("6. Udostępnij Listę")
    print("7. Powrót")

def process_menu_page(shopping_list, user_manager):
    db = Database()
    db.load_data("products_database.xlsx")
    q_calculator = QuantityCalculator(shopping_list, db)
    p_calculator = PriceCalculator(shopping_list, db)
    while True:
        q_calculator.calculate_quantity()
        p_calculator.calculate_price()
        menu_page()
        option = choose_option(8)
        if option == 1:
            process_adding(shopping_list)
        elif option == 2:
            if not shopping_list._products:
                print("Brak produktów na liście zakupów.")
                continue
            shopping_list.show_list()
            product_name = input("Podaj nazwę produktu do usunięcia: ")
            shopping_list.remove_product(product_name)
            print(f"Produkt '{product_name}' został usunięty z listy zakupów.")
        elif option == 3:
            if not shopping_list._products:
                print("Brak produktów na liście zakupów.")
                continue
            shopping_list.show_list()
            product_name = input("Podaj nazwę produktu do oznaczenia jako kupiony: ")
            shopping_list.mark_as_bought(product_name)
            print(f"Produkt '{product_name}' został oznaczony jako kupiony.")
        elif option == 4:
            shopping_list.show_list()
        elif option == 5:
            total_price = shopping_list.get_total_price()
            print(f"Całkowity koszt niekupionych zakupów: {total_price:.2f} PLN")
        elif option == 6:
            user_email = input("Podaj adres e-mail użytkownika, któremu chcesz udostępnić listę: ")
            shopping_list.share_with_user(user_email, user_manager)
            print(f"Lista zakupów została udostępniona użytkownikowi {user_email}.")
        elif option == 7:
            break

def process_adding(shopping_list):
    """
    Dodaje produkt do listy zakupów.
    :param shopping_list: Lista zakupów
    :param product_name: Nazwa produktu do dodania
    """
    while True:
            prod_name = input(" Wprowadź nazwę produktu lub 'done': ").lower()
            if prod_name == 'done': break

            prod_type = input("Podaj rodzaj produktu: 'drink' lub 'food': ").lower()
            if prod_type == 'drink':
                info_type = input("Wprowadzanie ilości - 'quantity' czy objętości - 'volume': ").lower()
                if info_type == 'quantity':
                    quantity = int(input("Wprowadź ilość butelek: "))
                    shopping_list.add_product(Drink(prod_name, quantity=quantity))
                elif info_type == 'volume':
                    volume = int(input("Wprowadź objętość napoju w ml: "))
                    shopping_list.add_product(Drink(prod_name, volume=volume))
            elif prod_type == 'food':
                info_type = input("Wprowadzanie ilości - 'quantity' czy masy - 'weight': ").lower()
                if info_type == 'quantity':
                    quantity = int(input("Wprowadź ilość sztuk: "))
                    shopping_list.add_product(Food(prod_name, quantity=quantity))
                elif info_type == 'weight':
                    weight = int(input("Wprowadź masę produktu w g: "))
                    shopping_list.add_product(Food(prod_name, weight=weight))
            else: # Generic product
                shopping_list.add_product(Product(prod_name))
            print(f"Produkt {prod_name} został dodany do listy zakupów.")