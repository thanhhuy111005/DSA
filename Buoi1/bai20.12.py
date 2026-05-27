a = [7, 3, 9, 12, 5, 8, 1]

min_value = a[0]
max_value = a[0]

min_index = 0
max_index = 0

for i in range(len(a)):

    if a[i] < min_value:
        min_value = a[i]
        min_index = i

    if a[i] > max_value:
        max_value = a[i]
        max_index = i

print("Min =", min_value)
print("Vi tri Min =", min_index)

print("Max =", max_value)
print("Vi tri Max =", max_index)