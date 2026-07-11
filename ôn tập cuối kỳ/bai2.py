A = [5,2,4,6,1,3]

shift = 0

for i in range(1, len(A)):
    key = A[i]
    j = i - 1

    while j >= 0 and A[j] > key:
        A[j + 1] = A[j]
        shift += 1
        j -= 1

    A[j + 1] = key

print("Mảng sau sắp xếp:", A)
print("Tổng số lần Shift:", shift)