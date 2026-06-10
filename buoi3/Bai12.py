a = ['abc', 'a', 'ab']

n = len(a)

for i in range(n - 1):
    for j in range(0, n - i - 1):
        if len(a[j]) > len(a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)