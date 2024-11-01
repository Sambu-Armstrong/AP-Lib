
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

    # Adding new books and members
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


library = Library()

# Adding new books
b1 = Book(1, "The Night Circus", 219, "Erin Morgenstern", "Fiction")
library.add_book(b1)
b2 = Book(2, "Algebra", 250, "Michael Artin", "Academic")
library.add_book(b2)
b3 = Book(3, "The Martian", 250, "Andy Weir", "Fiction")
library.add_book(b3)

# Adding a new  member
member1 = Member(1, "Armstrong")
member2 = Member(2, "Dane")
library.add_member(member1)
library.add_member(member2)

# Borrowing a book
library.borrow_book(1, 2)  # 1 represents member(Armstrong) and 2 book(Algebra)
library.borrow_book(2, 3)  # 2 represents member(Dane) and 3 book(The Martian)
library.list_books()

#returning a book
library.return_book(1, 2)  # Armstrong returns Algebra
library.list_books()


