def bai_8(a, i):
    """Tìm chỉ số phần tử nhỏ nhất trong đoạn [i, n)[cite: 26, 27]."""
    min_idx = i
    for j in range(i + 1, len(a)):
        if a[j] < a[min_idx]: min_idx = j
    return min_idx

