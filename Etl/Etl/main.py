from datetime import date

from entities.book import Book
from entities.customer import Customer
from entities.order import Order
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository
from repositories.Book_repository import BooksRepository
from repositories.import_repository import importRepository
from userInterface import userInterface


books_Repository = BooksRepository()
Customer_Repository = CustomerRepository()
Order_Repository = OrderRepository()
importar = importRepository()
user_interface = userInterface(Customer_Repository , Order_Repository, books_Repository)

importar.import_src(books_Repository)



while True:
    retorno = user_interface.stop()
    
    if retorno == 0:
        break
    elif retorno == 1:
        print(user_interface.Register_customer())
    elif retorno == 2:
        print(user_interface.Place_order())
    elif retorno == 3:
        print(user_interface.Order_Report())
    elif retorno == 4:
        print(user_interface.Customer_Report())
    elif retorno == 5:
        print(user_interface.Books_Report()) 
    elif retorno == 6:
        print(user_interface.verify_book())
    else: 
        print("Algo deu errado, Desligando sistema . . .")
        break
    
    