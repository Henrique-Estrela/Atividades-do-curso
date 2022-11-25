from datetime import date

from entities.book import Book
from entities.customer import Customer
from entities.order import Order
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository
from repositories.Book_repository import BooksRepository
from repositories.import_repository import import_repository


class userInterface:
    def __init__(self, Customer_Repository: CustomerRepository, Order_Repository: OrderRepository, books_Repository: BooksRepository) -> None:
        self.Customer_Repository = Customer_Repository
        self.Order_Repository = Order_Repository
        self.books_Repository = books_Repository
        
    
        
    def principal_menu(self) -> int:
        try:
            print("1 - Cadastrar cliente")
            print("2 - Fazer pedido")
            print("3 - Relatório de Pedidos")
            print("4 - Relatório de Clientes")
            print("5 - Relatório de Livros")
            print("0 - Sair")
            return int(input("Informe a opção do menu: "))
        except:
            print("A opção informada é inválida, o programa vai ser encerrado...")
            return 0

    def stop(self):
        result = self.principal_menu()
        if result == 0 or result > 5 or result < 0:
            return True
            
        return self.verify_result(result)

    def verify_result(self, retorno):
        
        if retorno == 1:
           return self.Register_customer()
        elif retorno == 2:
           return self.Place_order()
        elif retorno == 3:
            return self.Order_Report()
        elif retorno == 4:
            return self.Customer_Report()
        elif retorno == 5:
            return self.Books_Report()
        else:
            return 0


    
              

    def Register_customer(self):  
        id = int(input("Informe o código do cliente: "))
        nome = input("Informe o nome do cliente: ")
        customer = Customer(id, nome)
        self.Customer_Repository.list_customers.append(customer)
       
        return  print("Client cadastrado com sucesso!")


    def Place_order(self):
            id = int(input("Informe o código do pedido: "))
            customer_id = int(input("Informe o código do cliente: "))
            today = date.today()
            if (not self.Customer_Repository.verif_if_customer_exists(customer_id)):
                print("Cliente não existe!")
            else:
                customer = self.Customer_Repository.get_customer(customer_id)
                book_id = int(input("Informe o código do livro: "))

                if (not self.books_Repository.verif_if_book_exists(book_id)):
                    print("Livro não existe!")
                

                book = self.books_Repository.get_book(book_id)
                order = Order(id, customer, today)
                order.purchased_book = book

                self.Order_Repository.list_orders.append(order)
                print("Pedido cadastrado com sucesso!")


    def Order_Report(self):

            print("\n***** Relatório de pedidos *****\n")
            for order in self.Order_Repository.list_orders:
                if Book.verify_stock == False:
                    print("Já foi pego!")
                else:
                    print(f"Código do Pedido: {order.id}")
                    print(f"Cliente: {order.customer.name}")
                    print(f"Data do pedido: {order.date_order}")
                    print(f"Livro escolhido: {order.purchased_book.name} \n")


    def Customer_Report(self):

            formatText = "{0:<10} {1:<20}\n"
            menu = ("\n***** Relatório de clientes *****\n")
            menu += formatText.format("Id", "Cliente")

            for customer in self.Customer_Repository.list_customers:
                menu += formatText.format(customer.id, customer.name)
            print(menu)


    
    def Books_Report(self):

            formatText = "{0:<10} {1:<20} {1:<20} {1:<20} {1:<20} {1:<20}\n"
            menu = ("\n***** Relatório de livros cadastrados *****\n")
            menu += formatText.format("Id", "Ttítulo", "ISBN",
                                    "Autor", "Assunto", "Valor", "Estoque")

            for book in self.books_Repository.list_books:
                menu += formatText.format(book.id, book.name, book.isbn,
                                        book.author, book.category, book.price, book.stock)
            print(menu)
