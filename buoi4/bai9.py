def bai_9(a):
    """Double selection sort: mỗi vòng tìm cả phần tử nhỏ nhất và lớn nhất để đưa về đầu và cuối[cite: 29, 30]."""
    n = len(a)
    for i in range(n // 2):
        min_idx = max_idx = i
        for j in range(i + 1, n - i):
            if a[j] < a[min_idx]: min_idx = j
            if a[j] > a[max_idx]: max_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        if max_idx == i: max_idx = min_idx  # Xử lý biên khi max trùng vị trí đầu [cite: 68, 70]
        a[n - 1 - i], a[max_idx] = a[max_idx], a[n - 1 - i]
    return a

