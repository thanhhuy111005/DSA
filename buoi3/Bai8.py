a = [3, 2, 1]
k = 1

n = len(a)

for i in range(k):
    for j in range(0, n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

da_sap_xep = True

for i in range(n - 1):
    if a[i] > a[i + 1]:
        da_sap_xep = False
        break

print(da_sap_xep)