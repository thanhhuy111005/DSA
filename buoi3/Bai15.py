a = [('An', 8), ('Ba', 9), ('Cu', 8)]

n = len(a)

for i in range(n - 1):
    for j in range(0, n - i - 1):

        if a[j][1] < a[j + 1][1]:
            a[j], a[j + 1] = a[j + 1], a[j]

        elif a[j][1] == a[j + 1][1]:
            if a[j][0] > a[j + 1][0]:
                a[j], a[j + 1] = a[j + 1], a[j]

print(a)