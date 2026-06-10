a = [5, 1, 4, 2, 8]

start = 0
end = len(a) - 1
so_luot = 0

while start < end:
    so_luot += 1

    for i in range(start, end):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]

    end -= 1

    for i in range(end, start, -1):
        if a[i] < a[i - 1]:
            a[i], a[i - 1] = a[i - 1], a[i]

    start += 1

print("Mảng sau sắp xếp:", a)
print("Số lượt:", so_luot)