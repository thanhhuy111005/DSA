def cau_8():
    print("\n--- Câu 8. Bubble sort tối ưu (early-exit) ---")
    a = [1, 2, 3, 4]
    print(f"Mảng kiểm tra: {a}")

    def optimized_bubble_sort(arr):
        nums = list(arr)
        n = len(nums)
        passes = 0
        for i in range(n):
            swapped = False
            passes += 1
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:  # Dừng ngay nếu một lượt không phát sinh hoán đổi
                break
        return nums, passes

    _, total_passes = optimized_bubble_sort(a)
    print(f"-> Số lượt quét cần thiết trước khi dừng: {total_passes}")
