from entities.order import Order


class OrderRepository:
    def __init__(self) -> None:
        self.list_orders: list[Order] = []


    def verif_if_order_exists(self, id: int) -> bool:
        for book in self.list_orders:
            if (book.id == id):
                return True

        return False
    
    def verif_if_order_book_exists(self, name) -> bool:
        for book in self.list_orders:
            if (book.purchased_book.name == name):
                return True
        return False
    
    def name(self, id: int):
        for book in self.list_orders:
            if (book.id == id):
                return book.purchased_book.name