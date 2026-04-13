## 📚 Library Management System (Python)

A simple and clean Library Management System built using Python, focusing on Object-Oriented Programming (OOP) concepts and real-world logic.

---

## 🔍 Overview

- This project allows users to manage a collection of books with operations like adding, removing, searching, and displaying books.

- It is designed to practice clean coding and understand how real-world systems can be implemented using Python.

---

## ⚙️ Features

- 📖 Add new books  
- ❌ Remove books  
- 🔍 Search books  
- 📚 Display all books  
- 🔢 Automatic count using `len()`  

---

## 🧱 Concepts Used

- Classes and Objects  
- Encapsulation  
- List Data Structure  
- Conditional Logic  

---

## 💡 Design Approach

Instead of storing a separate variable for the number of books, the system dynamically calculates it using:

```python
len(self.books)
```

### This ensures:
-  Data consistency
-  Cleaner code
- Reduced bugs
- Better programming practices
##  🚀 Example Usage
```
library = Library()

library.add_book("Book1")
library.add_book("Book2")

library.search_book("Book1")
library.details()
```
## 🛠️ How to Run
- Install Python (3.x)
- Run the Python file:
```python main.py```
## 🔮 Future Improvements
- Menu-driven CLI system
- File handling (save/load data)
- GUI version (Tkinter / Web App)
- Database integration
## 📌 Conclusion

This project demonstrates how basic programming concepts can be applied to build a structured and useful system.

## 👨‍💻 Author

Nikhil Kumar