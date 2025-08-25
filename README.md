# 🛒 Smart Shopping List Manager (CLI)

A console-based application for creating, managing, and sharing shopping lists. This tool allows users to register accounts, manage multiple lists, and add products with specific attributes. It features an intelligent calculation system that can automatically determine the required quantity and total price of products based on a local product database.

---

## ✨ Key Features

* **User Management**: Simple registration and login system based on email.
* **Multiple Lists**: Each user can create, own, and delete multiple shopping lists.
* **List Sharing**: Seamlessly share any of your shopping lists with other registered users.
* **Smart Product Calculation**:
    * **Quantity Automation**: If you specify a total desired weight (e.g., 500g of apples) or volume (e.g., 2000ml of cola), the application automatically calculates the number of packages to buy based on the product database.
    * **Price Automation**: Automatically calculates the total price for the required quantity of each item.
* **Dynamic Product Types**: Add generic products, or specify them as `Food` (by weight) or `Drink` (by volume).
* **Status Tracking**: Mark items on your list as "bought" to keep track of your shopping progress.
* **Cost Estimation**: Calculate the total cost of all un-purchased items on your list at any time.

---

## 🔧 Setup and Installation

To get this project up and running on your local machine, follow these simple steps.

### Prerequisites

* Python 3.x
* `pip` (Python package installer)

### Installation Steps

1.  **Clone the repository:**

2.  **Install the required Python packages:**
    The project uses the `pandas` library to interact with the Excel database. You'll also need `openpyxl` for `.xlsx` file support.
    ```sh
    pip install pandas openpyxl
    ```

3.  **Create the Product Database:**
    The application relies on an Excel file named `products_database.xlsx` in the same directory as `app.py`. Create this file with the following columns:

    | nazwa                | objętość opakowania [ml] | masa produktu [g] | cena za opakowanie |
    | -------------------- | ------------------------ | ----------------- | ------------------ |
    | `Product Name`       | `Volume per package`     | `Weight per item` | `Price per package`|
    
    **Important:** The column headers must match exactly. Product names in the `nazwa` column should be in **lowercase** to ensure they are found by the application.

    **Example `products_database.xlsx`:**
    | nazwa | objętość opakowania [ml] | masa produktu [g] | cena za opakowanie |
    |-------|--------------------------|-------------------|--------------------|
    | woda  | 1500                     |                   | 1.99               |
    | cola  | 2000                     |                   | 6.49               |
    | mleko | 1000                     |                   | 3.20               |
    | chleb |                          | 500               | 4.50               |
    | jabłka|                          | 150               | 0.80               |

---

## 🚀 How to Run

Execute the `main.py` script from your terminal to start the application:

```sh
python main.py
```

---

## 📖 Usage Guide

The application is fully interactive through the command line.

1.  **Login/Register**: When you first run the app, you can choose to log in, register a new account, or exit.
    * **Registering** requires a name and an email address.
    * **Logging in** requires the email you registered with.

2.  **User Menu**: After logging in, you can:
    * Create a new shopping list.
    * Delete one of your existing lists.
    * View your own lists or lists shared with you.
    * Select a list to view and manage its contents.

3.  **List Management Menu**: Once you select a list, you can perform several actions:
    * **Add a Product**:
        * You'll be prompted for the product name and type (`food` or `drink`).
        * For `food`, you can specify a total desired `weight` or a specific `quantity` (number of items).
        * For `drink`, you can specify a total desired `volume` or a specific `quantity` (number of bottles/cans).
        * If the product exists in your `products_database.xlsx`, its quantity and price will be calculated automatically.
    * **Remove a Product**: Delete an item from the list.
    * **Mark as Bought**: Change a product's status to "bought".
    * **View List**: Display all products, their quantities, prices, and status.
    * **Get Total Cost**: See the sum of prices for all items not yet marked as "bought".
    * **Share List**: Enter another user's email to give them access to your list.

---

## 🏗️ Project Structure

The code is organized into several classes, each with a distinct responsibility, promoting modularity and maintainability.

shopping_list_app/
│
├── main.py # Entry point of the program. It initializes the UserManager, LoginManager, and ShoppingListManager classes and contains the main application loop. It handles user login/registration and then directs the user to the appropriate pages based on their choice.
├── calculators.py # This file contains classes for performing calculations on shopping list items. The QuantityCalculator determines the number of packages needed for a product based on its volume or weight and the package size available in the database. The PriceCalculator then calculates the total price for each product by multiplying the quantity by the package price from the database.
├── products_database.xlsx # Database of products with weights, volumes, and prices
├── checkers.py # This module defines a set of checker classes used for data validation. It uses an abstract base class Checker to establish a common interface. Concrete classes like QuantityChecker, VolumeChecker, WeightChecker, PriceChecker, and StatusChecker are used to validate product attributes, ensuring they meet specific criteria before being used in calculations or display.
├── data_management.py # This module handles interactions with the product database. The Database class uses the pandas library to load product information from an Excel file. It provides methods to find products by name and retrieve their package prices.
├── list_management.py # This file contains the ShoppingListManager class, which is responsible for creating and removing shopping lists. It holds a dictionary of ShoppingList objects, allowing the application to manage multiple lists, and also provides a method for displaying lists.
├── product.py # This file defines the product data structure. The base Product class holds common attributes like name, quantity, price, and status. It is extended by the Drink and Food classes, which add specific attributes like volume for drinks and weight for food items.
├── shopping_list.py # This module defines the ShoppingList class, which represents a single shopping list. It allows for adding, removing, and marking products as bought. It also includes methods to display the list's contents, calculate the total price of unbought items, and share the list with other users. It uses helper functions and classes from other modules to perform checks and calculations.
├── ui_functions.py # This file contains all the functions responsible for the user interface and interaction. It provides functions to display menus, process user input, and handle different pages of the application, such as the login page, the user's main page, and the shopping list menu. It acts as the bridge between the user and the application's core logic.
├── user_management.py # This module manages users and their data. The Person class represents a user, storing their name, email, and lists they own or have access to. The UserManager handles adding and retrieving users from a dictionary, while the LoginManager facilitates user login and registration processes.

* **Models (`Product`, `Food`, `Drink`, `Person`)**
    * These classes represent the core data entities of the application. `Food` and `Drink` inherit from the base `Product` class. `Person` holds user data and their associated lists.

* **Managers (`ShoppingListManager`, `UserManager`, `LoginManager`)**
    * These classes handle the application's business logic. They manage collections of objects (like users and lists) and orchestrate user actions like registration, login, and list creation.

* **Core Logic (`ShoppingList`)**
    * This is the central class for an individual shopping list. It contains the list of products and methods to add, remove, and manage them.

* **Data and Calculation (`Database`, `QuantityCalculator`, `PriceCalculator`)**
    * `Database`: A wrapper around `pandas` to load and query the `products_database.xlsx` file.
    * `QuantityCalculator` & `PriceCalculator`: These classes encapsulate the logic for automatically calculating product quantities and prices by cross-referencing the shopping list with the database.

* **Validation (`Checker` and subclasses)**
    * A set of simple classes that follow the Strategy pattern to validate product attributes (like quantity and price) before displaying them, ensuring the output is clean and logical.

* **User Interface (`..._page` and `process_...` functions)**
    * A series of functions that handle all console input and output, creating the interactive menu-driven experience for the user.

---

## 🔮 Future Improvements

* **Data Persistence**: Save user accounts and shopping lists to a file (e.g., JSON, SQLite) so that data is not lost when the application closes.
* **Graphical User Interface (GUI)**: Rebuild the application with a graphical framework like Tkinter or PyQt for a more user-friendly experience.
* **Enhanced Error Handling**: Implement more robust error handling to prevent crashes from invalid user input.
* **Unit Testing**: Add a comprehensive suite of unit tests to ensure the reliability and correctness of each component.
* **Refactoring**: Separate the UI logic from the business logic more strictly, potentially by moving the `process_...` functions into dedicated controller classes.

## Contributing

Feel free to fork this repository and submit pull requests to improve features or add new ones.