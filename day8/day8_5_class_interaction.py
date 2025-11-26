# Day 8 - Exercise 5: Class Interaction Example

class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author  # This is an Author object

    def description(self):
        print(f"'{self.title}' by {self.author.name}")

# Create objects
author1 = Author("George Orwell")
book1 = Book("1984", author1)

author2 = Author("J.K. Rowling")
book2 = Book("Harry Potter and the Sorcerer's Stone", author2)

# Print descriptions
book1.description()
book2.description()
