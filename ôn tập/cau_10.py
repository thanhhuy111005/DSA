def cau_10():
    print("\n--- Câu 10. Binary insertion sort ---")
    a = [3, 2, 1]

    def binary_insertion_sort(arr):
        nums = list(arr)
        for i in range(1, len(nums)):
            key = nums[i]
            # Dùng Tìm kiếm nhị phân tìm vị trí chèn lý tưởng
            low, high = 0, i
            while low < high:
                mid = (low + high) // 2
                if nums[mid] <= key:
                    low = mid + 1
                else:
                    high = mid
            
            # Số phép dịch chuyển (Shift) hoàn toàn giữ nguyên không đổi
            for j in range(i, low, -1):
                nums[j] = nums[j - 1]
            nums[low] = key
        return nums

    print(f"Mảng gốc: {a} -> Sau khi chạy Binary Insertion Sort: {binary_insertion_sort(a)}")
    print("Phân tích: Số phép so sánh giảm xuống O(log i) nhưng số phép dịch chuyển (shift) GIỮ NGUYÊN do bản chất bộ nhớ.")
