def cau_6():
    print("\n--- Câu 6. Chia mảng tổng lớn nhất nhỏ nhất ---")

    def split_array(nums, k):
        def can_split(max_sum):
            current_sum = 0
            segments = 1
            for num in nums:
                if current_sum + num > max_sum:
                    segments += 1
                    current_sum = num
                    if segments > k:
                        return False
                else:
                    current_sum += num
            return True

        low = max(nums)
        high = sum(nums)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if can_split(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    a = [7, 2, 5, 10, 8]
    k = 2
    print(f"Mảng: {a}, k = {k} -> Tổng lớn nhất nhỏ nhất sau khi chia: {split_array(a, k)}")


# ==============================================================================
# 2. THUẬT TOÁN SẮP XẾP VÀ PHÂN TÍCH CẤU TRÚC
# ==============================================================================
