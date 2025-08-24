from user_management import UserManager, LoginManager
from list_management import ShoppingListManager
from ui_functions import login_page, process_login_page, process_user_page, process_menu_page, choose_option


def main():
    user_manager = UserManager()
    login_manager = LoginManager(user_manager)
    list_manager = ShoppingListManager()
    user = None
    while True:
        if user:
            shopping_list = process_user_page(user, option, list_manager)
            if shopping_list:
                process_menu_page(shopping_list, user_manager)
        else:
            login_page()
            option = choose_option(3)
            user = process_login_page(option, login_manager)


if __name__ == "__main__":
    main()