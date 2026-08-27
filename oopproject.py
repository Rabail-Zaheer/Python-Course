# Create the Book class
class Book:

    # Constructor
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    # Method to borrow the book
    def borrow(self):
        self.is_borrowed = True
        print(self.title, "has been borrowed.")

    # Method to return the book
    def return_book(self):
        self.is_borrowed = False
        print(self.title, "has been returned.")


# Create 3 Book objects
book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("Matilda", "Roald Dahl")


# Borrow books
book1.borrow()
book2.borrow()

# Return books
book1.return_book()
book2.return_book()

# Borrow and return the third book
book3.borrow()
book3.return_book()