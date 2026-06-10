import random

n = 10000
k = 3

a = list(range(n))

for i in range(n):
    j = min(n - 1, i + random.randint(0, k))
    a[i], a[j] = a[j], a[i]

so_luot = 0
so_swap = 0

for i in range(n - 1):
    hoan_doi = False
    so_luot += 1

    for j in range(0, n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            so_swap += 1
            hoan_doi = True

    if hoan_doi == False:
        break

print("Số lượt:", so_luot)
print("Số swap:", so_swap)