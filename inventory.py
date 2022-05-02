class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.books = [] ##empty list for books

class Books:
    def __init__(self, name, id, quantity, price ):
        self.name = name
        self.id = id
        self.quantity = quantity
        self.price = price

##formula showing complete price of same book
    @property
    def combinedPrice(self):
        return f'${self.quantity * self.price:.2f}'

##class to show the books id, price, and name
    def show(self):
        id = 1
        for book in self.books:
            print(str(f'{id} -> [x{book.price}] {book.name}'))
            index += 1