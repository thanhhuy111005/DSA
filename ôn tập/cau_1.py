def cau_1():
    print("\n--- Câu 1. Tìm kiếm cơ bản ---")

    def binary_search(arr, x):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    a = [1, 3, 5, 7, 9]
    x = 7
    print(f"Mảng: {a}, x = {x} -> Chỉ số tìm thấy: {binary_search(a, x)}")
