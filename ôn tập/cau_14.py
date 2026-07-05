def cau_14():
    print("\n--- Câu 14. Shell sort ---")
    a = [9, 8, 3, 7, 5, 6, 4, 1]
    print(f"Mảng gốc: {a}")

    def shell_sort(arr):
        nums = list(arr)
        n = len(nums)
        gap = n // 2  # Dãy gap giảm dần mẫu: 4, 2, 1
        while gap > 0:
            for i in range(gap, n):
                key = nums[i]
                j = i
                while j >= gap and nums[j - gap] > key:
                    nums[j] = nums[j - gap]
                    j -= gap
                nums[j] = key
            gap //= 2
        return nums

    print(f"Mảng sau khi sắp xếp qua Shell Sort: {shell_sort(a)}")


# ==============================================================================
# 3. ĐỒ THỊ & THUẬT TOÁN DIJKSTRA TỐI ƯU
# ==============================================================================
