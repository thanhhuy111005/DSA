A = [12, 5, 7, 1, 9]
x = 1

for i in range(len(A)):

    if A[i] == x:
        print("Tìm thấy", x, "tại vị trí", i)
        break
    
    
    
    
    A = [1, 3, 5, 7, 9, 12]

x = 7

left = 0
right = len(A) - 1

while left <= right:

    mid = (left + right) // 2

    if A[mid] == x:
        print("Tìm thấy", x, "tại vị trí", mid)
        break

    elif A[mid] < x:
        left = mid + 1

    else:
        right = mid - 1