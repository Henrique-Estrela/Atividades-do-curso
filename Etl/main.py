from datetime import date

from entities.book import Book
from entities.customer import Customer
from entities.order import Order
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository
from repositories.Book_repository import BooksRepository
from repositories.import_repository import import_repository
from userInterface import userInterface


books_Repository = BooksRepository()
Customer_Repository = CustomerRepository()
Order_Repository = OrderRepository()
importar = import_repository()
user_interface = userInterface(Customer_Repository , Order_Repository, books_Repository)

importar.import_src(books_Repository)

# menu_option = user_interface.principal_menu()


while True:
    retorno = user_interface.stop()
    if retorno == True:
        break

    

        

