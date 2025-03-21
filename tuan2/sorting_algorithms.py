'''
Bài tập 1 (sorting_algorithms):
So sánh hiệu suất sắp xếp cơ bản
o Tạo một mảng ngẫu nhiên có 1000 phần tử
o Chạy cả 3 thuật toán trên cùng một mảng đầu vào
o Đo thời gian thực thi của mỗi thuật toán
o Hiển thị mẫu dữ liệu đã sắp xếp
'''
import random as rd
import time

from sorting import bubble_sort
from sorting import selection_sort
from sorting import insertion_sort

def measure_time(sort_function, arr):
    start_time = time.time()
    # if sort_function == quick_sort or sort_function == merge_sort:
    #     sorted_arr = sort_function(arr)
    # else:
    sort_function(arr)
        
    end_time = time.time()
    return end_time - start_time

num = [rd.randint(0, 1000) for _ in range(1000)]

bubble_list = num.copy()
selection_list = num.copy()
insertion_list = num.copy()

print(f"Bubble Sort: {measure_time(bubble_sort, bubble_list):.6f}s\n")
print(f"Selection Sort: {measure_time(selection_sort, selection_list):.6f}s\n")
print(f"Insertion Sort: {measure_time(insertion_sort, insertion_list):.6f}s\n")
print(f"Mau da sap xep: {bubble_list[:10]}")     