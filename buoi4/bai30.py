def bai_30(a):
    """Sắp xếp tăng dần và đếm tổng số lần dịch chuyển phần tử (shift)[cite: 111, 112]."""
    shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            shifts += 1
        a[j + 1] = key
    return shifts

