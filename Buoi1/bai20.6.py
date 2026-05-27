def linear_search(a, x):

    for i in range(len(a)):

        if a[i] == x:
            return i

    return -1


a = [7, 3, 9, 12, 5, 8, 1]

x = int(input("Nhap x: "))

ket_qua = linear_search(a, x)

print(ket_qua)