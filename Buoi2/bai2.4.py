def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    
    while (left <= right):
        mid = (left + right) // 2
        
        if (arr[mid] == key):
            return mid
        if (key < arr[mid]):
            right = mid - 1
        else:
            left = mid + 1
            
    return -1

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

key_a = 95
result_a = binary_search(arr, key_a)
print("Cau a - Vi tri cua x=95 la:", result_a)

key_b = 5
result_b = binary_search(arr, key_b)
print("Cau b - Vi tri cua x=5 la:", result_b)