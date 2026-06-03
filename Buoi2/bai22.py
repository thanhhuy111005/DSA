a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = sorted(a + b)
n = len(c)

if n % 2 == 1:
    print(float(c[n // 2]))
else:
    print((c[n // 2 - 1] + c[n // 2]) / 2)