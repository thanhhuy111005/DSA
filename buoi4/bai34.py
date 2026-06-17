def bai_34(a):
    """Binary insertion sort: dùng tìm kiếm nhị phân để giảm số so sánh xuống O(log i)[cite: 124, 125]."""
    for i in range(1, len(a)):
        key = a[i]
        pos = bisect.bisect_right(a, key, 0, i)
        for j in range(i, pos, -1):
            a[j] = a[j - 1]
        a[pos] = key
    return a

