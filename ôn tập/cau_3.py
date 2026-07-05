def cau_3():
    print("\n--- Câu 3. Lower / Upper bound ---")

    def lower_bound(arr, x):
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                high = mid
            else:
                low = mid + 1
        return low

    def upper_bound(arr, x):
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid] > x:
                high = mid
            else:
                low = mid + 1
        return low

    a = [1, 3, 5, 7]
    x = 4
    print(f"Mảng: {a}, x = {x}")
    print(f"Lower bound (Phần tử nhỏ nhất >= {x}): idx {lower_bound(a, x)}")
    print(f"Upper bound (Phần tử nhỏ nhất > {x}): idx {upper_bound(a, x)}")
