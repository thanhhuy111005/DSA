A = [7, 3, 9, 12, 5, 8, 1]
x = 5

for i in range(len(A)):

    print("Bước", i + 1)
    print("i =", i)
    print("A[i] =", A[i])

    if A[i] == x:
        print(A[i], "==", x, "=> Đúng")
        print("Đã tìm thấy", x, "tại vị trí", i)
        break

    else:
        print(A[i], "==", x, "=> Sai")
        print("Tiếp tục\n")