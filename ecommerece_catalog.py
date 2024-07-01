import random

# Task 1: Create Base Product Class
# Develop a base class Product with common attributes like product ID, name, price, and a method to display product information.
# Expected Outcome: A Product class that can hold general information about a product and display it.

class Product:
    def __init__(self,name,price, product_id):
        self.name = name
        self.price = price
        self.product_id = product_id

    def product_info(self):
        print(f'''
        Product: {self.name}
        Price: ${self.price}
        ''')

# (ONLY BOOK SUBCLASS REQUIRED)
# Create subclasses Book, Electronic, and Clothing that inherit from Product.
# Each subclass should have additional attributes relevant to its category (e.g., author for books, specs for electronics, size for clothing).
# Expected Outcome: Each subclass contains both inherited attributes from Product and new attributes specific to the product type.

class Book(Product):
    def __init__(self,author,name, price,product_id):
        super().__init__(name,price,product_id)
        self.author = author



# Task 3: Override Display Method in Subclasses

# Override the method to display product information in each subclass to include specific attributes.
# For example, the Book class should display the author, Electronic should display specs, etc.
# Expected Outcome: Calling the display method on an instance of any subclass shows both common and specific product details.

    def book_info(self):
        print(f'''
        Book: {self.name} by {self.author}
        This price for this book: {self.price}
        Book Serial #{self.product_id}
        ''')

# Instantiate objects of each subclass and call their display methods to ensure correct information is shown.
# Expected Outcome: The system should accurately display detailed information for each type of product, demonstrating inheritance and method overriding.

if __name__ == "__main__":
    peach = Product("Peach","1.69",1010)
    peach.product_info()
    print("-"*25)
    mb4u = Book("Joyce Meyers","Me Before You","$10.89",1003)
    mb4u.book_info()


