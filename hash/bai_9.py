def bai_9():
    print("\n--- Bài 9. Two Sum dùng hash ---")
    arr = [2, 7, 11, 15]
    target = 9
    print(f"Mảng: {arr}, Target: {target}")

    def two_sum(nums, tgt):
        seen = {}  # Map lưu: giá trị -> chỉ số chỉ định
        for i, num in enumerate(nums):
            comp = tgt - num
            if comp in seen:
                return (seen[comp], i)
            seen[num] = i
        return None

    print(f"Kết quả cặp chỉ số tìm được: {two_sum(arr, target)}")
