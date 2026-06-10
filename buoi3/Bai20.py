def merge_sort(a):
    if len(a) <= 1:
        return a, 0

    mid = len(a) // 2

    left, inv_left = merge_sort(a[:mid])
    right, inv_right = merge_sort(a[mid:])

    merged = []
    i = 0
    j = 0
    inv_count = inv_left + inv_right

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged, inv_count


a = [2, 3, 1]

sorted_a, swaps = merge_sort(a)

print("Số swap của Bubble Sort:", swaps)
print("Mảng sau sắp xếp:", sorted_a)