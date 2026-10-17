import csv
class Book:
    def __init__(self,name,author,date):
        self.name = name
        self.author = author
        self.date = date
    def display(self):
       print(f'Book_name : {self.name:<35} , Book_author : {self.author:<25} , Publish_data : {self.date}')   

class LibraryManager:
    def __init__(self):
        self.books = []
        self.load_from_csv()

    def load_from_csv(self, filename="books.csv"):
        try:
            with open(filename, "r") as f:
                reader = csv.reader(f)
                next(reader, None)  
                for row in reader:
                    if len(row) == 3:  
                        self.books.append(Book(row[0], row[1], row[2]))
        except FileNotFoundError:
            print("CSV file nahi mili, naya database start ho raha hai.")



    def save_to_csv(self, filename="books.csv"):
        try:
            with open(filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Name", "Author", "Date"])  
                for b in self.books:
                    writer.writerow([b.name, b.author, b.date])
            print("Data save ho gaya!")
        except PermissionError:
            print("Error: File open hai, pehle band karein.")
        
    def add_book(self,name,author,date):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Book name valid string honi chahiye!")
        found = False
        for book in self.books:
            if book.name.strip().lower() == name.strip().lower():
                print("book already exist")
                found = True
                break
        if not found: 
            book_new = Book(name.strip(),author,date)
            self.books.append(book_new)
            print(f"book {name} added successfully")
            self.save_to_csv()
            
                
    
    def remove_book(self,name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Book name valid string honi chahiye!")
        found = False
        for book in self.books:
            if book.name.strip().lower() == name.strip().lower():
                self.books.remove(book)
                print(f"book : {name} removed successfully")
                self.save_to_csv()
                found = True
                break
        if not found: 
            print("book not exist")

    def search_book(self,name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Book name valid string honi chahiye!")
        found = False
        for book in self.books:
            if book.name.strip().lower() == name.strip().lower():
                print("book found ")
                book.display()
                found =True
                break
        if not found:
            print(f"book : {name} not found")
                
    def display_all(self):
        found = False
        for  book in self.books:
            if book:
                book.display()
                found =True
        if not found:
            print("library empty")




library1 = LibraryManager()
library1.add_book("Chunotiya Mujhe Pasand Hai","Sudesh Dhankhar",2015)
library1.add_book("The One: Cricket, My Life And More","Shikhar Dhawan",2015)
library1.add_book("The Great Sanctions Hack", "Urjit Patel’s",2015)
library1.add_book("Wings of Valour","Swapnil Pandey",2015)
library1.add_book("Above and Beyond", "Shiv Kumar Mohanka",2015)

library1.add_book("Maine Cancer Ko Jeet Liya", "Dr. P. Vijay Anand Reddy",2015)



library1.display_all()


library1.search_book("above and beyond")

library1.remove_book("above and beyond")
