from entities.book import Book


class BooksRepository:
    def __init__(self) -> None:
        self.list_books: list[Book] = []
        

        
    def verif_if_book_exists(self, book_id: int) -> bool:
        for book in self.list_books:
            if (book.id == book_id):
                return True

        return False
    

    def get_book(self, book_id: int):
        for book in self.list_books:
            if (book.id == book_id):
                return book

        return Book(-1, "Book not found!", "", "", "", 0)
    
    def verif_if_total_price_exists(self, id: int) -> bool:
        for book in self.list_books:
            if (book.id == id and book.price == 0): 
                return False
        return True

    def verify_stock(self, id) -> bool:
        for book in self.list_books:
            if (book.id == id and book.stock > 0):
                    return True
        return False
            
 

    def baixar_estoque(self, name) -> bool:
        for book in self.list_books:
            if (book.name == name):
                book.stock -= 1
                return True
        return False
            

    
