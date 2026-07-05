def cau_2():
    print("\n--- Câu 2. Vị trí đầu/cuối & đếm ---")

    def find_first_last_count(arr, x):
        def find_first():
            low, high = 0, len(arr) - 1
            res = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == x:
                    res = mid
                    high = mid - 1  # Tiếp tục dò sang bên trái
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return res

        def find_last():
            low, high = 0, len(arr) - 1
            res = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == x:
                    res = mid
                    low = mid + 1  # Tiếp tục dò sang bên phải
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return res

        dau = find_first()
        cuoi = find_last()
        dem = 0 if dau == -1 else (cuoi - dau + 1)
        return dau, cuoi, dem

    a = [1, 2, 2, 2, 3]
    x = 2
    dau, cuoi, dem = find_first_last_count(a, x)
    print(f"Mảng: {a}, x = {x} -> Đầu: {dau}, Cuối: {cuoi}, Tổng đếm: {dem}")
