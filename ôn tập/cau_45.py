def cau_45():
    print("\n--- Câu 45. Tổng đoạn con bằng k ---")
    a = [1, 1, 1]
    k = 2

    def subarray_sum(nums, target_k):
        prefix_map = {0: 1}
        curr_sum = 0
        count = 0
        for num in nums:
            curr_sum += num
            if curr_sum - target_k in prefix_map:
                count += prefix_map[curr_sum - target_k]
            prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1
        return count

    print(f"Mảng: {a}, k = {k} -> Số đoạn con thỏa mãn: {subarray_sum(a, k)}")
