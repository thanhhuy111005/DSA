def bai_12():
    print("\n--- Bài 12: Loại bỏ trùng lặp giữ thứ tự ---")
    arr = [3, 1, 3, 2, 1]
    print(f"Mảng có trùng lặp: {arr}")

    # Cách O(n) dùng tập băm (Set) để kiểm tra nhanh
    seen = set()
    result = []
    for x in arr:
        if x not in seen:
            seen.add(x)
            result.append(x)

    print(f"Kết quả loại bỏ trùng lặp (giữ nguyên thứ tự): {result}")
