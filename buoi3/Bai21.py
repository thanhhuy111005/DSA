a = [(2, 'a'), (1, 'b'), (2, 'c'), (1, 'd')]

n = len(a)

stable = a.copy()

for i in range(n - 1):
    for j in range(0, n - i - 1):
        if stable[j][0] > stable[j + 1][0]:
            stable[j], stable[j + 1] = stable[j + 1], stable[j]

unstable = sorted(a, key=lambda x: (x[0], -ord(x[1])))

print("Bubble Sort ổn định:")
print(stable)

print("Thuật toán không ổn định:")
print(unstable)