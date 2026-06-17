def bai_15(a, k):
    """Sắp xếp một phần (k nhỏ nhất): Thực hiện đúng k vòng selection và trả về mảng[cite: 51, 52, 53]."""
    n = len(a)
    for i in range(min(k, n)):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]: min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a[:k]

