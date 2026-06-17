def bai_4(a):
    """In trạng thái mảng sau mỗi vòng chọn[cite: 12, 13]."""
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]: min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        print(f"Vòng {i+1}: {a}")

