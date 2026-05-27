a = [7, 3, 9, 12, 5, 8, 1]

max_value = a[0]
vi_tri = 0

for i in range(len(a)):

    if a[i] > max_value:
        max_value = a[i]
        vi_tri = i

print("Gia tri lon nhat:", max_value)
print("Vi tri:", vi_tri)