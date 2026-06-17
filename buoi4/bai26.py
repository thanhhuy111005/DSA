def bai_26(a, x):
    """Chèn một phần tử vào mảng đã sắp xếp tăng dần sao cho mảng vẫn tăng dần[cite: 97, 98, 99]."""
    a.append(0)
    i = len(a) - 2
    while i >= 0 and a[i] > x:
        a[i + 1] = a[i]
        i -= 1
    a[i + 1] = x
    return a

