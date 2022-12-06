from datetime import date

from entities.book import Book
from entities.customer import Customer
from entities.order import Order
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository
from repositories.Book_repository import BooksRepository
from repositories.import_repository import importRepository
from userInterface import userInterface


def test_baixar_estoque():

    Customer_Repository = CustomerRepository()
    Books_Repository = BooksRepository()
    importar = importRepository()

    importar.import_src(Books_Repository)


    customer = Customer(1, "Henrique")
    Customer_Repository.list_customers.append(customer)


    today = date.today()
    book = Books_Repository.get_book(1)
    order = Order(1, customer, today)


    order.purchased_book = book
    verify = Books_Repository.baixar_estoque(order.purchased_book.name)


    assert verify == True


def test_verif_if_customer_exists():
    
    Customer_Repository = CustomerRepository()


    customer = Customer(1, "Henrique")
    Customer_Repository.list_customers.append(customer)    

    customer2 = Customer(1, "Leonardo")

    verify = Customer_Repository.verif_if_customer_exists(customer2.id)


    assert verify == True


def test_verif_if_order_exists():
    Order_Repository = OrderRepository()
    Customer_Repository = CustomerRepository()
    books_Repository = BooksRepository()
    id = 1
    
    customer = Customer(1, "Henrique")
    Customer_Repository.list_customers.append(customer)   
    today = date.today()
    
    customer = Customer_Repository.get_customer(customer.id)
    book = books_Repository.get_book(1)
    order = Order(id, customer, today)
    order.purchased_book = book

    Order_Repository.list_orders.append(order)
    books_Repository.baixar_estoque(order.purchased_book.name)

    verify = Order_Repository.verif_if_order_exists(1)
           
    assert verify == True


def test_verif_if_total_price_existsh():
    Customer_Repository = CustomerRepository()
    books_Repository = BooksRepository()
    importar = importRepository()

    importar.import_src(books_Repository)
    
    customer = Customer(1, "Henrique")
    Customer_Repository.list_customers.append(customer)   
    today = date.today()
    
    customer = Customer_Repository.get_customer(customer.id)
    book_id = 2
    
    verify = books_Repository.verif_if_total_price_exists(book_id)


           
    assert verify == False


def test_verif_field_customer_exists():
    Customer_Repository = CustomerRepository()
    Order_Repository = OrderRepository()
    Books_Repository = BooksRepository()

    user_Interface = userInterface(Customer_Repository, Order_Repository, Books_Repository)
    
    verify = user_Interface.Place_order()
           
    assert verify == 'Acho que você esqueceu algum parametro vazio!'


def test_verif_field_book_exists():
    Customer_Repository = CustomerRepository()
    Order_Repository = OrderRepository()
    Books_Repository = BooksRepository()

    user_Interface = userInterface(Customer_Repository, Order_Repository, Books_Repository)
    
    verify = user_Interface.Place_order()
           
    assert verify == 'Acho que você esqueceu algum parametro vazio!'


def test_format_str_price_to_float():
    import_repository = importRepository()
    Books_Repository = BooksRepository()


    verify = import_repository.format_str_price_to_float('R$ 39$90')

    assert verify == 0


def test_verif_if_order_book_exists():

    Order_Repository = OrderRepository()
    Customer_Repository = CustomerRepository()
    Books_Repository = BooksRepository()
    importar = importRepository()

    importar.import_src(Books_Repository)


    customer = Customer(1, "Henrique")
    Customer_Repository.list_customers.append(customer)


    today = date.today()
    book = Books_Repository.get_book(1)
    order = Order(1, customer, today)


    order.purchased_book = book
    Order_Repository.list_orders.append(order)
    Books_Repository.baixar_estoque(order.purchased_book.name)



    verify = Order_Repository.verif_if_order_book_exists(Order_Repository.name(1))

    assert verify == True



def test_verif_stock():
    Books_Repository = BooksRepository()
    importar = importRepository()

    importar.import_src(Books_Repository)
    id = 100

    verify = Books_Repository.verify_stock(id)

    assert verify == True


def test_verif_if_book_exists():
    Books_Repository = BooksRepository()
    importar = importRepository()

    importar.import_src(Books_Repository)
    id = 100

    verify = Books_Repository.verif_if_book_exists(id)



    assert verify == True