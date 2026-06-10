a = [5, 1, 4, 2, 8]

n = len(a)

for i in range(n):

    for j in range(0, n - i - 1):

        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print("Mang sau khi sap xep tang dan la:")
print(a)