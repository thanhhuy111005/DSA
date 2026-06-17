def bai_6(a):
    """Sắp xếp tăng dần và đếm số lần so sánh (luôn dùng n(n-1)/2 so sánh)[cite: 19, 20, 21]."""
    n = len(a)
    comparisons = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_idx]: min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return comparisons

