def bai_3(a):
    """Sắp xếp mảng theo thứ tự giảm dần, mỗi vòng chọn phần tử lớn nhất[cite: 9, 10]."""
    n = len(a)
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if a[j] > a[max_idx]: max_idx = j
        a[i], max_idx = max_idx, a[i]
    return a

