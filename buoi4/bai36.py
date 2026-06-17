def bai_36(a):
    """Sắp xếp tăng dần theo |a[i]|, bằng nhau giữ nguyên thứ tự xuất hiện (ổn định)[cite: 133, 134]."""
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and abs(a[j]) > abs(key):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

