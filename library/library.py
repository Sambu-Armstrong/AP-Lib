import tkinter as tk
from tkinter import simpledialog, messagebox


class Lib_Item:
    def __init__(self, id, title):
        self._id = id
        self._title = title

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title
    
    def borrow_book(self):
        pass
    
    def return_book(self):
        pass
    



class Book(Lib_Item):
    def __init__(self, id, title, size, author, genre, available=True):
        super().__init__(id, title)
        self._size = size
        self._author = author
        self._genre = genre
        self._available = available

    @property
    def size(self):
        return self._size

    @property
    def author(self):
        return self._author

    @property
    def genre(self):
        return self._genre

    @property
    def available(self):
        return self._available

    #sets the book to borrowed
    def borrow_book(self):
        if self._available:
            self._available = False
            return True
        else:
            return False

    #sets the book to available
    def return_book(self):
        self._available = True


class Member:
    def __init__(self, member_no, name):
        self._member_no = member_no
        self._name = name
        self._borrowed_books = []

    @property
    def member_no(self):
        return self._member_no

    @property
    def name(self):
        return self._name
    
    #borrowing a book from the lib
    def borrow_book(self, book):
        if book.borrow_book():
            self._borrowed_books.append(book)
            print(f"{self._name} borrowed the book {book.title}")
        else:
            print(f"{book.title} is not available")

    #returning a borrowed book
    def return_book(self, book):
        if book in self._borrowed_books:
            book.return_book()
            self._borrowed_books.remove(book)
            print(f"{book.title} has been returned")
        else:
            print(f"{self._name} did not borrow {book.title}")


class Library:
    def __init__(self):
        self._books = []
        self._members = []

    # Adding new books and members to the library
    def add_book(self, book):
        self._books.append(book)
        print(f"{book.title} has been added to the Library {book.genre} section")

    def add_member(self, member):
        self._members.append(member)
        print(f"{member.name} is now a member")

    #shows a list of all books and showing  their details and status(whether it's borrowed or available)
    def list_books(self):
        for book in self._books:
            status = "available" if book.available else "borrowed"
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Size: {book.size} pages, Status: {status}")


    # a method to borrow a book
    def borrow_book(self, member_no, book_id):
        member = next((m for m in self._members if m.member_no == member_no), None)
        book = next((b for b in self._books if b.id == book_id), None)
        if member and book:
            member.borrow_book(book)
        else:
            print("Invalid member number or book ID")

            
    # returning a borrowed book
    def return_book(self, member_no, book_id):
        member = next((m for m in self._members if m.member_no == member_no), None)
        book = next((b for b in self._books if b.id == book_id), None)
        if member and book:
            member.return_book(book)
        else:
            print("Invalid member number or book ID")




#A simple GUI for the library system
class LibraryGUI:
    #setting up the GUI window 
    def __init__(self, root):
        self.library = Library() #initializing the library
        self.root = root    #setting the root window
        self.root.title("Library System")
        
        self.setup_gui()

    #adding buttons to the GUI window
    def setup_gui(self):
        tk.Button(self.root, text="Add Book", command=self.add_book).pack(pady=20)
        tk.Button(self.root, text="Add Member", command=self.add_member).pack(pady=20)
        tk.Button(self.root, text="Borrow Book", command=self.borrow_book).pack(pady=20)
        tk.Button(self.root, text="Return Book", command=self.return_book).pack(pady=20)
        tk.Button(self.root, text="List Books", command=self.list_books).pack(pady=20)
    
    def add_book(self):
        id = simpledialog.askinteger("Input", "Enter Book ID:")
        title = simpledialog.askstring("Input", "Enter Book Title:")
        size = simpledialog.askinteger("Input", "Enter Book Size (pages):")
        author = simpledialog.askstring("Input", "Enter Book Author:")
        genre = simpledialog.askstring("Input", "Enter Book Genre:")
        book = Book(id, title, size, author, genre)
        self.library.add_book(book)
    
    def add_member(self):
        member_no = simpledialog.askinteger("Input", "Enter Member ID:")
        name = simpledialog.askstring("Input", "Enter Member Name:")
        member = Member(member_no, name)
        self.library.add_member(member)

    def borrow_book(self):
        member_no = simpledialog.askinteger("Input", "Enter Member ID:")
        book_id = simpledialog.askinteger("Input", "Enter Book ID:")
        self.library.borrow_book(member_no, book_id)

    def return_book(self):
        member_no = simpledialog.askinteger("Input", "Enter Member ID:")
        book_id = simpledialog.askinteger("Input", "Enter Book ID:")
        self.library.return_book(member_no, book_id)

    def list_books(self):
        books = '\n'.join([f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Size: {book.size} pages, Status: {'available' if book.available else 'borrowed'}" for book in self.library._books])
        messagebox.showinfo("Library Books", books)

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()


