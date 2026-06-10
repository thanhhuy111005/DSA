a = [4, 2, 7, 1, 3]

n = len(a)

for i in range(n - 1):

    if a[i] > a[i + 1]:
        a[i], a[i + 1] = a[i + 1], a[i]

print(a[n - 1])