a = [2, 3, 1]

n = len(a)

swap = 0
nghich_the = 0

for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            nghich_the += 1

b = a.copy()

for i in range(n - 1):
    for j in range(0, n - i - 1):
        if b[j] > b[j + 1]:
            b[j], b[j + 1] = b[j + 1], b[j]
            swap += 1

print("Số nghịch thế:", nghich_the)
print("Số lần hoán đổi:", swap)
print("Mảng sau sắp xếp:", b)