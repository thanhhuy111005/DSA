def bai_32(a):
    """Dùng insertion sort sắp xếp một mảng ký tự theo bảng chữ cái[cite: 117, 118]."""
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

