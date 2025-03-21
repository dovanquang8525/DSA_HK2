'''
Bài tập 3 (library_management):
Quản lý thông tin sách, mỗi sách có: ID (tự động tăng), tên, tác
giả, năm xuất bản, giá, số lượng.
Sử dụng dictionary để lưu trữ dữ liệu ID sách được tạo tự động
theo định dạng B001, B002,...zz
Các chức năng chính:
o Thêm sách mới
o Hiển thị danh sách sách
o Sắp xếp theo: Tên sách (Bubble Sort), Năm xuất bản (Insertion
Sort), Giá sách (Selection Sort).
o Tìm kiếm sách (theo ID hoặc tên)
o Mượn/trả sách với kiểm tra số lượng
'''
from sorting import bubble_sort
from sorting import selection_sort
from sorting import insertion_sort

class Book:
    def __init__(self, id, ten_sach, tac_gia, nam_xuat_ban, gia, so_luong):
        self.id = id
        self.ten_sach = ten_sach
        self.tac_gia = tac_gia
        self.nam_xuat_ban = nam_xuat_ban
        self.gia = gia
        self.so_luong = so_luong
    
    def book_info(self):
        print("\n === BOOK INFORMATION === ")
        print(f"ID: B0{self.id}")
        print(f"Ten sach: {self.ten_sach}")
        print(f"Tac gia: {self.tac_gia}")
        print(f"Nam xuat ban: {self.nam_xuat_ban}")
        print(f"Gia: {self.gia}")
        print(f"So luong: {self.so_luong}")

class QuanLySach:
    def __init__(self):
        self.books = []
        self.id = 0
    def them_sach(self):
        self.id += 1
        ten_sach = input("Nhap ten sach: ")
        tac_gia = input("Nhap ten tac gia: ")
        nam_xuat_ban = int(input("Nam xuat ban: "))     
        while True:
            try:
                gia = float(input("Gia: "))
                if gia < 0:
                    print(" --- Vui long nhap lai --- ")
                    continue
                break
            except ValueError:
                print("Loi nhap")
                
        while True:
            try:
                so_luong = int(input("So luong: "))
                if so_luong < 0:
                    print(" --- Vui long nhap lai --- ")
                    continue
                break
            except ValueError:
                print("Loi nhap")
        
        book = Book(self.id, ten_sach, tac_gia, nam_xuat_ban, gia, so_luong)
        
        self.books.append(book)
        print("\n --- Them thanh cong --- ")

    def display_book(self):
        if not self.books:
            print("\n NOTHING HERE ")
        else:
            for _ in self.books:
                Book.book_info(_)
    
    def bubble_sort_Name(self):
        name_list = [book.ten_sach for book in self.books]
        bubble_sort(name_list)
        for book, name in zip(self.books, name_list):
            print("\n === BOOK INFORMATION === ")
            print(f"ID: {book.id}")
            print(f"Ten sach: {name}")
            print(f"Tac gia: {book.tac_gia}")
            print(f"Nam xuat ban: {book.nam_xuat_ban}")
            print(f"Gia: {book.gia}")
            print(f"So luong: {book.so_luong}")
        
    def insert_sort_Year(self):
        year_list = [book.nam for book in self.books]
        insertion_sort(year_list)
        for book, year in zip(self.books, year_list):
            print("\n === BOOK INFORMATION === ")
            print(f"ID: {book.id}")
            print(f"Ten sach: {book.ten_sach}")
            print(f"Tac gia: {book.tac_gia}")
            print(f"Nam xuat ban: {year}")
            print(f"Gia: {book.gia}")
            print(f"So luong: {book.so_luong}")
    
    def selection_sort_Price(self):
        price_list = [book.gia for book in self.books]
        selection_sort(price_list)
        for book, price in zip(self.books, price_list):
            print("\n === BOOK INFORMATION === ")
            print(f"ID: {book.id}")
            print(f"Ten sach: {book.ten_sach}")
            print(f"Tac gia: {book.tac_gia}")
            print(f"Nam xuat ban: {book.nam_xuat_ban}")
            print(f"Gia: {price}")
            print(f"So luong: {book.so_luong}")
    def tim_kiem_theo_ID(self):
        id = int(input("Nhap ID de tim kiem: "))
        for book in self.books:
            if book.id == id:
                Book.book_info(book)
            else:
                print("Nothing found")
    def muon_sach(self):
        return
        
def menu():
    print('1. Thêm sách mới')
    print('2. Hiển thị danh sách sách')
    print('3. Sắp xếp theo: Tên sách (Bubble Sort), Năm xuất bản (Insertion Sort), Giá sách (Selection Sort)')
    print('4. Tìm kiếm sách (theo ID hoặc tên)')
    print('5. Mượn sách')
    print('6. Trả sách')
    print('7. Thoát')
    quanLy = QuanLySach()
    
    while True:
        try:
            n = int(input("Nhap lua chon: "))
            if n == 1:
                quanLy.them_sach()
            elif n == 2:
                quanLy.display_book()
            elif n == 3:
                key = input("Sap xep theo (name, year, price): ")
                if key == "name":
                    quanLy.bubble_sort_Name()
                elif key == "year":
                    quanLy.insert_sort_Year()
                elif key == "price":
                    quanLy.selection_sort_Price()
            elif n == 4:
                quanLy.tim_kiem_theo_ID()
            elif n == 5:
                quanLy.muon_sach()
            elif n == 6:
                quanLy.tra_sach()
            elif n == 7:
                break
        except ValueError:
            print("Loi nhap")
menu()