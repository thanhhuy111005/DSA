def cau_4():
    print("\n--- Câu 4. Tìm trong mảng xoay ---")

    def search_rotated(arr, x):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                return mid

            # Kiểm tra xem nửa bên trái có được sắp xếp tuần tự không
            if arr[low] <= arr[mid]:
                if arr[low] <= x < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Ngược lại, nửa bên phải được sắp xếp tuần tự
            else:
                if arr[mid] < x <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

    a = [4, 5, 6, 7, 0, 1, 2]
    x = 0
    print(f"Mảng xoay: {a}, x = {x} -> Vị trí tìm thấy: {search_rotated(a, x)}")
