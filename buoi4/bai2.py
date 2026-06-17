def bai_2(a):
    """Sắp xếp mảng số nguyên theo thứ tự tăng dần bằng Selection Sort[cite: 5, 6]. Ràng buộc: n <= 10^3[cite: 8]."""
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]: min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

