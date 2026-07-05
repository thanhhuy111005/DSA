def cau_46():
    print("\n--- Câu 46. Dãy liên tiếp dài nhất ---")
    a = [100, 4, 200, 1, 3, 2]
    print(f"Mảng đầu vào: {a}")

    num_set = set(a)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:  # Điểm bắt đầu chuỗi
            curr = num
            streak = 1
            while curr + 1 in num_set:
                curr += 1
                streak += 1
            longest = max(longest, streak)

    print(f"-> Độ dài chuỗi số nguyên liên tiếp dài nhất: {longest}")


# ==============================================================================
# 9. HÀM BĂM CHUYÊN SÂU & THUẬT TOÁN ĐIỀU PHỐI
# ==============================================================================
