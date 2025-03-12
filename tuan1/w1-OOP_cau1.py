# Câu 1 
# Xây dựng một hệ thống quản lý thư viện đơn giản với các yêu cầu sau:
# • Tạo class Book với các thuộc tính: title, author, isbn, status (available/borrowed)
# • Tạo class Library để quản lý danh sách sách với các phương thức: 
# o add_book(): Thêm sách mới
# o remove_book(): Xóa sách theo ISBN
# o borrow_book(): Mượn sách
# o return_book(): Trả sách
# o display_books(): Hiển thị danh sách sách
def display_library_menu():
    print("\n=== LIBRARY MANAGEMENT SYSTEM ===")
    print("1. Add new book")
    print("2. Remove book")
    print("3. Borrow book")
    print("4. Return book")
    print("5. Display all book")
    print("6. Search book by ISBN")
    print("7. Exit\n")
    # return input("Enter your choice 1-7")

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = 'available'
    def display_book_information(self):
        print(f"\n--- BOOK'S INFORMATION ---")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"status: {self.status}")

class Library:
    # books = []
    def __init__(self):
        self.books = []
    # add_book():
    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            print("\nAdd successfull")
        else:
            print("\nFail !!")
    # remove_book()
    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print("\nRemove successfull")
            else:
                print("\nFail !!")
    # borrow_book()
    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.status == 'available':
                book.status = 'borrowed'
                print("\nBorrowed successfull")
            else:
                print("\nBook has been borrowed")
    # return_book()
    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.status == 'borrowed':
                book.status = 'available'
                print("\nReturned successfull")
            else:
                print("\nBook has been returned")
    # search_book()
    def search_book(self, isbn):
        for book in self.books:
            if  book.isbn == isbn:
                print(book)
                book.display_book_information()
                break
            else:
                print("\nNothing here")
    # display_books()
    def display_books(self):
        if not self.books:
            print("Nothing here")
        else:
            for book in self.books:
                book.display_book_information()

library = Library()
while True:
    display_library_menu()
    n = int(input("Enter your choice 1-7: "))
    if n == 1:
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        library.add_book(Book(title, author, isbn))
    elif n == 2:
        isbn = input("ISBN: ")
        library.remove_book(isbn)
    elif n == 3:
        isbn = input("ISBN: ")
        library.borrow_book(isbn)
    elif n == 4:
        isbn = input("ISBN: ")
        library.return_book(isbn)
    elif n == 5:
        library.display_books()
    elif n == 6:
        isbn = input("ISBN: ")
        library.search_book(isbn)
    elif n == 7:
        break
        