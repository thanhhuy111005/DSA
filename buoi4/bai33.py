def bai_33(a, k):
    """Thực hiện k vòng chèn đầu tiên rồi in mảng[cite: 120, 121]."""
    for i in range(1, min(k + 1, len(a))):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

