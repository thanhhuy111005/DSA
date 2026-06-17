def bai_7(a):
    """Dùng selection sort sắp xếp một mảng ký tự theo bảng chữ cái[cite: 23, 24]."""
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]: min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

