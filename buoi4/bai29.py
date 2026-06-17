def bai_29(a):
    """In trạng thái mảng sau mỗi vòng lặp ngoài (chèn xong phần tử thứ i)[cite: 107, 108]."""
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        print(f"Bước chèn {i}: {a}")

