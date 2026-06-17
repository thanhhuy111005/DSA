def bai_17(a, k):
    """Phần tử nhỏ thứ k (partial selection): Chạy k vòng selection, O(n*k)[cite: 58, 59, 60]."""
    n = len(a)
    for i in range(k):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]: min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a[k - 1]

