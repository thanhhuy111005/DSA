def cau_34():
    print("\n--- Câu 34. Loại bỏ trùng lặp giữ thứ tự ---")
    a = [3, 1, 3, 2, 1]
    print(f"Mảng trùng: {a}")

    # Phương pháp tối ưu O(n) dùng tập băm (Set) để dò quét
    seen = set()
    res = []
    for num in a:
        if num not in seen:
            seen.add(num)
            res.append(num)

    print(f"Kết quả loại trùng giữ nguyên thứ tự xuất hiện đầu tiên: {res}")
