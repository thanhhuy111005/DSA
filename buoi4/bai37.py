def bai_37(a):
    """Dùng insertion sort sắp xếp danh sách chuỗi tăng dần theo độ dài[cite: 136, 137]."""
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and len(a[j]) > len(key):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

