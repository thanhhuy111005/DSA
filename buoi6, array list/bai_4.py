def bai_4():
    print("\n--- Bài 4: Tìm kiếm tuyến tính ---")
    arr = [5, 3, 7]
    print(f"Mảng: {arr}")

    def index_of(target):
        for i in range(len(arr)):  # Quét tuyến tính O(n)
            if arr[i] == target:
                return i
        return -1

    print(f"Tìm kiếm giá trị 7 -> Kết quả index: {index_of(7)}")
    print(f"Tìm kiếm giá trị 9 -> Kết quả index: {index_of(9)}")
