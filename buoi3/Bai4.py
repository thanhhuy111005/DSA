a = [3, 2, 1]

n = len(a)

count = 0

for i in range(n):

    for j in range(0, n - i - 1):

        if a[j] > a[j + 1]:

            a[j], a[j + 1] = a[j + 1], a[j]

            count += 1

print("Mang sau khi sap xep la:")
print(a)

print("Tong so lan hoan doi la:", count)