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
    

    # def format_str_price_to_float(self, price: str) -> float:
    #     try:
    #         return float(price.replace("R$ ", "").replace(",", "."))
    #     except:
    #         return 0
            

    
