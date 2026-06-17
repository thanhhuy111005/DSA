def bai_16(a):
    """Sắp xếp tăng dần theo |a[i]| bằng selection sort[cite: 55, 56]."""
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if abs(a[j]) < abs(a[min_idx]): min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

