# Write MyBook class, which inherits from Book
class MyBook(Book):
    def __init__(self, title, author, price):
        # Use super to call the constructor in the parent class
        super().__init__(title, author)
        self.price = price
        
    def display(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Price: {self.price}')
