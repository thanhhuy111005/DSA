def vi_tri_cuoi(a, x):

    for i in range(len(a) - 1, -1, -1):

        if a[i] == x:
            return i

    return -1


a = [7, 5, 3, 5, 9, 5]

x = int(input("Nhap x: "))

print(vi_tri_cuoi(a, x))