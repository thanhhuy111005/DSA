def bai_12(a):
    """Selection sort ổn định: thay vì swap, dịch chuyển phần tử nhỏ nhất về vị trí đúng[cite: 40, 41]."""
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]: min_idx = j
        key = a[min_idx]
        while min_idx > i:
            a[min_idx] = a[min_idx - 1]
            min_idx -= 1
        a[i] = key
    return a

