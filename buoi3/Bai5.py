a = [1, 2, 3]

n = len(a)

count_compare = 0

for i in range(n):

    for j in range(0, n - i - 1):

        count_compare += 1

        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)

print("Tong so lan so sanh la:", count_compare)