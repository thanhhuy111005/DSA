start = [4, 3, 2, 1]
target = [3, 2, 1, 4]

a = start.copy()

n = len(a)
so_luot = 0

while a != target:
    for j in range(0, n - so_luot - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

    so_luot += 1

print("Số lượt ít nhất:", so_luot)
print("Trạng thái đạt được:", a)