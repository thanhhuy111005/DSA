def bai_13():
    print("\n--- Bài 13. Dãy liên tiếp dài nhất ---")
    arr = [100, 4, 200, 1, 3, 2]
    print(f"Mảng đầu vào: {arr}")

    num_set = set(arr)
    longest_streak = 0

    for num in num_set:
        # Nếu (num - 1) không có trong tập, chứng tỏ 'num' có thể là điểm bắt đầu chuỗi
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    print(f"Độ dài dãy số nguyên liên tiếp dài nhất: {longest_streak}")
