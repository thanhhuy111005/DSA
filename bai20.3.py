A = [7, 3, 9, 12, 5, 8, 1]
x = 7

count = 0

for i in range(len(A)):

    count += 1

    if A[i] == x:
        print("Tìm thấy", x)
        break

print("Số phép so sánh:", count)



A = [7, 3, 9, 12, 5, 8, 1]
x = 1

count = 0

for i in range(len(A)):

    count += 1

    if A[i] == x:
        print("Tìm thấy", x)
        break

print("Số phép so sánh:", count)





A = [7, 3, 9, 12, 5, 8, 1]
x = 100

count = 0
found = False

for i in range(len(A)):

    count += 1

    if A[i] == x:
        found = True
        print("Tìm thấy", x)
        break

if found == False:
    print("Không tìm thấy", x)

print("Số phép so sánh:", count)


