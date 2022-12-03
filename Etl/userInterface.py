from datetime import date


from entities.book import Book
from entities.customer import Customer
from entities.order import Order
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository
from repositories.Book_repository import BooksRepository
from repositories.import_repository import importRepository


class userInterface:
    def __init__(self, Customer_Repository: CustomerRepository, Order_Repository: OrderRepository, books_Repository: BooksRepository) -> None:
        self.Customer_Repository = Customer_Repository
        self.Order_Repository = Order_Repository
        self.books_Repository = books_Repository
        
    def style(self):
        return '⁀ ↘‿ ↗' * 5
        
    def principal_menu(self) -> int:
        try:
            print(self.style())
            print('''\n1 ↣ Cadastrar cliente \n2 ↣ Fazer pedido \n3 ↣ Relatório de Pedidos \n4 ↣ Relatório de Clientes \n5 ↣ Relatório de Livros \n6 ↣ Estoque de Livros \n0 ↣ Sair\n''')
            print(self.style())
            return int(input("\nInforme a opção do menu: "))
        except:
            print("\n↣ A opção informada é inválida, o programa vai ser encerrado...\n")
            return 0

    def stop(self):
        result = self.principal_menu()
        if result == 0 or result > 6 or result < 0:
            return 0
            
        return result
    
    

    def Register_customer(self):  
        try:
            id = int(input("Informe o código do cliente: "))
            if (self.Customer_Repository.verif_if_customer_exists(id)):
                return "O código do cliente já existe!"
            nome = input("Informe o nome do cliente: ")

            customer = Customer(id, nome)
            self.Customer_Repository.list_customers.append(customer)
        
            return "Client cadastrado com sucesso!"
        except:
            return "Acho que você esqueceu algum parametro vazio!"

    def Place_order(self):
            try:
                id = int(input("Informe o código do pedido: "))
                if (self.Order_Repository.verif_if_order_exists(id)):
                        return "O código do pedido já existe!"
                customer_id = int(input("Informe o código do cliente: "))
                today = date.today()

                if (not self.Customer_Repository.verif_if_customer_exists(customer_id)):
                    return "Cliente não existe!"

                
                customer = self.Customer_Repository.get_customer(customer_id)
                book_id = int(input("Informe o código do livro: "))

                if (not self.books_Repository.verif_if_book_exists(book_id)):
                    return "Livro não existe!"
            
                if(self.Order_Repository.verif_if_order_book_exists(self.Order_Repository.name(book_id))):
                    return "Livro Já foi pego"
           
                if (not self.books_Repository.verif_if_total_price_exists(book_id)):
                    return "Livro com preço errado!"

                book = self.books_Repository.get_book(book_id)
                order = Order(id, customer, today)
                order.purchased_book = book
            

                self.Order_Repository.list_orders.append(order)

                self.books_Repository.baixar_estoque(order.purchased_book.name)
                return "Pedido cadastrado com sucesso!"
            except:
                return "Acho que você esqueceu algum parametro vazio!"

            
    def Order_Report(self):

            # print("\n***** Relatório de pedidos *****\n")
            # for order in self.Order_Repository.list_orders:
            #         return f"Código do Pedido: {order.id} \nCliente: {order.customer.name} \nData do pedido: {order.date_order} \nLivro escolhido: {order.purchased_book.name} \n"
            print("\n***** Relatório de pedidos *****\n")
            for order in self.Order_Repository.list_orders:
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
            return menu


    
    def Books_Report(self):
          
        formatText = "{0:<10} {1:<20} {2:<20} {3:<20} {4:<20} {5:<20} {6:<5}\n"
        menu = ("\n***** Relatório de livros cadastrados *****\n")
        menu += formatText.format("Id", "Ttítulo", "ISBN",
                                "Autor", "Assunto", "Valor", "Estoque")

        for book in self.books_Repository.list_books:
            menu += formatText.format(book.id, book.name, book.isbn,
                                    book.author, book.category, book.price, book.stock)
        return menu

    def verify_book(self ):
            try:
                numId = int(input("Informe o código do Livro: "))
                if (not self.books_Repository.verify_stock(numId)):
                    return "Ainda tem estoque"
                return "Não existe livro disponivel"
            except:
                return "Algo deu errado, tente novamente!"