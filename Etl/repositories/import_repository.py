from entities.book import Book
from repositories.Book_repository import BooksRepository

class importRepository:

    file_book = list(open("books.csv", "r", encoding="utf-8"))
    
    

    def format_str_price_to_float(self, price: str) -> float: 
        try:
            return float(price.replace("R$ ", "").replace(",", "."))
        except:
            return 0

    def import_src(self, Books_Repository: BooksRepository):
        for book in self.file_book[1:]:
            list_book = book.split(";")
            book = Book(int(list_book[0]), list_book[1], list_book[2], list_book[3],
                        list_book[4], self.format_str_price_to_float(list_book[5]))
            Books_Repository.list_books.append(book)
            
            