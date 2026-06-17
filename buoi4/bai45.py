def bai_45(a):
    """Cài đặt Shell sort tổng quát hóa insertion sort với khoảng cách (gap) giảm dần[cite: 167, 168]."""
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            key = a[i]
            j = i
            while j >= gap and a[j - gap] > key:
                a[j] = a[j - gap]
                j -= gap
            a[j] = key
        gap //= 2
    return a

