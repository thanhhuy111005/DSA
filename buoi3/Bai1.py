a = [5, 1, 4, 2, 8]

n = len(a)

for i in range(n - 1):

    if a[i] > a[i + 1]:
        a[i], a[i + 1] = a[i + 1], a[i]

print("Mang sau 1 luot bubble sort la:")
print(a)