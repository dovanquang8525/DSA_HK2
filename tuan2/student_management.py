'''
Bài tập 2 (student_management):
Xây dựng hệ thống quản lý sinh viên, mỗi sinh viên có: MSSV, họ
tên, tuổi, và GPA
Các chức năng chính:
o Thêm sinh viên mới
o Hiển thị danh sách sinh viên
o Sắp xếp theo GPA (dùng Bubble Sort)
o Sắp xếp theo tên (dùng Insertion Sort)
o Sắp xếp theo tuổi (dùng Selection Sort)
o Tìm kiếm sinh viên theo MSSV
Xây dựng chương trình và chọn các tùy chọn từ menu. Xem danh sách
đã sắp xếp theo các tiêu chí khác nhau
'''
# from sorting import bubble_sort
# from sorting import selection_sort
# from sorting import insertion_sort

class Student:
    def __init__(self, mssv, hoVaTen, tuoi, gpa):
        self.mssv = mssv
        self.hoVaTen = hoVaTen
        self.tuoi = tuoi
        self.gpa = gpa
    
    def student_info(self):
        print("----------------------------------------------------------------")
        print(f"||{self.mssv} || {self.hoVaTen} || {self.tuoi} || {self.gpa}||")
        print("----------------------------------------------------------------")

        
class StudentManagement:
    def __init__(self):
        self.students = []
    
    def them_sinh_vien(self):
        mssv = int(input("Nhap MSSV: "))
        
        for student in self.students:
            if student.mssv == mssv:
                print("MSSV da ton tai")
                return

        hoVaTen = input("Nhap Ho va Ten sinh vien: ")
        
        while True:
            try:
                tuoi = int(input("Nhap tuoi: "))
                if tuoi < 16 or tuoi > 100:
                    print("Tuoi [16 - 100]")
                    continue
                break
            except ValueError:
                print("Nhap tuoi so nguyen")

        while True:
            try:
                gpa = float(input("Nhap GPA: "))
                if gpa < 0 or gpa > 4.0:
                    print("GPA [0.0 - 4.0]")
                    continue
                break
            except ValueError:
                print("GPA khong am")
        new_student = Student(mssv, hoVaTen, tuoi, gpa)
        self.students.append(new_student)
        print("\n --- Cap nhap thanh cong --- ")
        
    def danh_sach_sinh_vien(self):
        if not self.students:
            print(" --- Nothing here !! --- ")
        else:
            for student in self.students:
                Student.student_info(student)
            
    def bubble_sort_GPA(self):
        # gpa_list = [student.gpa for student in self.students]
        # bubble_sort(gpa_list)
        # for student, gpa in zip(self.students, gpa_list):
        #     print("----------------------------------------------------------------")
        #     print(f"||{student.mssv} || {student.hoVaTen} || {student.tuoi} || {gpa}||")
        #     print("----------------------------------------------------------------")
        arr = self.students.copy()
        n = len(arr)
        for i in range(n): # 0 -> n - 1
            for j in range(0, n - 1 - i): # 0 -> n - 1 - i
                if arr[j].gpa > arr[j+1].gpa:
                # Đổi chỗ giá trị tại 2 vị trí index
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        

        
    def insert_sort_ten(self):
        # name_list = [student.hoVaTen for student in self.studetns]
        # insertion_sort(name_list)
        # for student, name in zip(self.students, name_list):
        #     print("----------------------------------------------------------------")
        #     print(f"||{student.mssv} || {name} || {student.tuoi} || {student.gpa}||")
        #     print("----------------------------------------------------------------")
        arr = self.students.copy()
        for i in range(1, len(arr)):
            key = arr[i].hoVaTen
            j = i - 1
        
            while j >= 0 and key < arr[j].hoVaTen:
                arr[j + 1] = arr[j]
                j -= 1
            
            arr[j + 1] = key
        
    def selection_sort_tuoi(self):
        # age_list = [student.tuoi for student in self.students]
        # selection_sort(age_list)
        # for student, age in zip(self.students, age_list):
        #     print("----------------------------------------------------------------")
        #     print(f"||{student.mssv} || {student.hoVaTen} || {age} || {student.gpa}||")
        #     print("----------------------------------------------------------------")
        arr = self.students.copy()
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[j].tuoi < arr[min_index].tuoi:
                    min_index = j
                # Đổi chỗ giá trị tại 2 vị trí index
            arr[i], arr[min_index] = arr[min_index], arr[i]
        
    def tim_kiem_theo_MSSV(self):
        mssv = int(input("Nhap MSSV de tim kiem: "))
        for student in self.students:
            if student.mssv == mssv:
                Student.student_info(student)
            else:
                print("MSSV khong ton tai")
                
def menu():
    quanly = StudentManagement()
    print("\n --- HE THONG QUAN LY SINH VIEN --- ")
    print("1. Them sinh vien moi")
    print("2. Hien thi danh sach sinh vien")
    print("3. Sap xep theo GPA")
    print("4. Sap xep theo ten")
    print("5. Sap xep theo tuoi")
    print("6. Tim kiem sinh vien theo MSSV")
    print("0. Thoat\n")
    while True:
        # print("\n --- HE THONG QUAN LY SINH VIEN --- ")
        # print("1. Them sinh vien moi")
        # print("2. Hien thi danh sach sinh vien")
        # print("3. Sap xep theo GPA")
        # print("4. Sap xep theo ten")
        # print("5. Sap xep theo tuoi")
        # print("6. Tim kiem sinh vien theo MSSV")
        # print("0. Thoat\n")
        
        try:
            n = int(input("Nhap lua chon: "))
            
            if n == 1:
                quanly.them_sinh_vien()
            elif n == 2:
                quanly.danh_sach_sinh_vien()
            elif n == 3:
                quanly.bubble_sort_GPA()
            elif n == 4:
                quanly.insert_sort_ten()
            elif n == 5:
                quanly.selection_sort_tuoi()
            elif n == 6:
                quanly.tim_kiem_theo_MSSV()
            elif n == 0:
                break
        except Exception as e:
            print(f"Loi {e}")
menu() 

