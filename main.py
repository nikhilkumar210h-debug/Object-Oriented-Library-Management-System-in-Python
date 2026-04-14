# exercise - 6 (library management system)

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            len(self.books)
            print("Book added✅")
        else:
            print("Book already added!")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            len(self.books)
            print("✅ Book removed!")
        else:
            print("❌ Book not found!!")

    def search_book(self, book):
        if book in self.books:
            print("✅ Book available")
        else:
            print("❌ Book not found!!")


    def details(self):
        print(f"\n📚 Total books: {len(self.books)}")
        if not self.books:
            print("No books available")
        else:
            for book in self.books:
                print("-", book)

library1 = Library()

library2 = Library()
library2.add_book("book1")
library2.add_book("book2")
library2.add_book("book3")
library2.add_book("book4")
library2.add_book("book5")
library2.add_book("book6")
library2.details()

library1.add_book("book1")
library1.add_book("book2")
library1.add_book("book3")
library1.add_book("book4")
library1.add_book("book5")

library1.search_book("book2")

library1.details()
