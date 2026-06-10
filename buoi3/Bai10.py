a = [2, 1, 3, 4]

n = len(a)
so_luot = 0

for i in range(n - 1):
    hoan_doi = False
    so_luot += 1

    for j in range(0, n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            hoan_doi = True

    if hoan_doi == False:
        break

print("Số lượt cần thiết:", so_luot)
print("Mảng sau sắp xếp:", a)