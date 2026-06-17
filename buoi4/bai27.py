def bai_27(a):
    """Sắp xếp mảng số nguyên theo thứ tự tăng dần bằng Insertion Sort[cite: 101, 102]. Ràng buộc: n <= 10^3[cite: 103]."""
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

