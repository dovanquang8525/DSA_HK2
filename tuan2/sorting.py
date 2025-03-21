'''
Bubble Sort (sắp xếp nổi bọt)
'''

def bubble_sort(arr):
    
    n = len(arr)
    
    for i in range(n): # 0 -> n - 1
        for j in range(0, n - 1 - i): # 0 -> n - 1 - i
            if arr[j] > arr[j+1]:
                # Đổi chỗ giá trị tại 2 vị trí index
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
                #? 1 cách làm khác cho việc đổi chỗ -> đặt biến tạm
                # temp = arr[j]
                # arr[j] = arr[j + 1]
                # arr[j + 1] = temp
                

'''
Insertion Sort (sắp xếp chèn)
'''

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key

'''
Selection Sort (sắp xếp chọn)
'''

def selection_sort(arr):
    
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Đổi chỗ giá trị tại 2 vị trí index
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
        #? 1 cách làm khác cho việc đổi chỗ
        # temp = arr[i]
        # arr[i] = arr[min_index]
        # arr[min_index] = temp

