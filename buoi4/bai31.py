def bai_31(a):
    """Sắp xếp tăng dần và đếm tổng số lần so sánh giữa các phần tử[cite: 114, 115]."""
    comparisons = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = key
    return comparisons

