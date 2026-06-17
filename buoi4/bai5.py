def bai_5(a):
    """Sắp xếp tăng dần và đếm số lần hoán đổi (tối đa n-1 swap)[cite: 16, 17]."""
    n = len(a)
    swaps = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]: min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        swaps += 1
    return swaps

