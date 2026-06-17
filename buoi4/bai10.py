def bai_10(a):
    """Chỉ hoán đổi khi phần tử nhỏ nhất khác vị trí hiện tại và đếm số swap thực sự[cite: 33, 34]."""
    n = len(a)
    exact_swaps = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]: min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            exact_swaps += 1
    return exact_swaps

# --- LÝ THUYẾT SELECTION SORT ---

