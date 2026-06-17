def bai_28(a):
    """Sắp xếp mảng theo thứ tự giảm dần sử dụng Insertion Sort[cite: 104, 105]."""
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] < key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

