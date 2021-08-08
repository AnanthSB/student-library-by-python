"""
implemented a student library system using oop.
Where a student can borrow, return and add books in the list books of the library."""


class library():
    
    def __init__(self,*arg):
        self.books = books
        self.borrowed = brbooks

    @property
    # This property function will return currently available books 
    def available_books(self):
        if self.books!= []:    
            return "\n".join((self.books))
        else:
            return '0'
        
    # This funtion takes a book and give to student and removes from the books list         
    def borrow(self):
        book = (input("Enter the book name to borrow: ")).upper()
        if book in self.books:
            print(f"\nYou have been issued the book '{book}'")
            (self.books).remove(f"{book}")
            (self.borrowed).append(f"{book}")
        else:
            print(f"\nCould not issue the book\nMay be issued to someone else or not available as of now.")

    # This function takes book and adds to the books list 
    def return_book(self):
        borrowed_books = "\n".join(self.borrowed) # used join method , joins every item of list by \n
        # print(borrowed_books)
        book = input(f"The books which are need to return:\n{borrowed_books}\nEnter book name to return\n").upper()
        if book not in self.books and book in (self.borrowed):
            print(f"\nThank you for returning the book '{book}'")
            #adds book to books list
            (self.books).append(f"{book}")
            #Removes book from borrowed list    
            (self.borrowed).remove(book)
        else:
            print(f"\nCouldn't return the book,May be it's not belongs to this library\nOR May be we had not issued this book to you")
    
    # This function does same as return function. adds new book into the books list
    def add_book(self):
        book = (input("Enter the book name to add: ")).upper()
        if book not in self.books:
            print(f"\nadded book: '{book}'")
            (self.books).append(f"{book}")
        else:
            print("This book may exist already\nOR can't take back")

       
"""____________________________________Here main starts____________________________________"""

books = ["C++","C","OOP","PYTHON"]
brbooks = []
# The Object instatioating to the library class(parent class)
student1 = library(books,brbooks)

message = """\n=============Welcome To Student Library System=============
Enter 1 to check available books\n      2 to borrow a book\n      3 to return a book\n      4 to Add a book\n      5 to exit"""

# function of calls handling
def call():
    global message, books
    choice = input(f"{message}\nEnter choice: ")
    
    if choice == '5' :
        print("\nThank you for using library\n______Have a nice day______")
        exit()
    elif choice == '1':
        print(student1.available_books)
    elif choice == '2':
        if student1.available_books != '0':
            print(f"Available books:\n{student1.available_books}")
            student1.borrow()
        else:
            print("Currently all books are issued to others\n  please visit after sometime")
    elif choice == '3':
        student1.return_book()
    elif choice == '4':
        student1.add_book()
    else:
        print("Choose the correct book name\nOrElse enter e to exit_ ")

    # While loop for for iterating the continue and exit options
    while True:
        inp = input("Enter 0 : continue or 5 : exit\n ")
        if inp == '0':
            call()
        elif inp == '5':
            print("\nThank you for using library\n______Have a nice day______")
            exit()
        else:
            print("Wrong input, try again")

call()
        
"""________________________________________THE_END________________________________________"""