def cau_44():
    print("\n--- Câu 44. Two Sum dùng hash ---")
    a = [2, 7, 11]
    target = 9

    def two_sum_hash(nums, tgt):
        seen = {}
        for i, num in enumerate(nums):
            comp = tgt - num
            if comp in seen:
                return (seen[comp], i)  # Trả về cặp chỉ số trong O(n)
            seen[num] = i
        return None

    print(f"Mảng: {a}, Target: {target} -> Chỉ số: {two_sum_hash(a, target)}")
