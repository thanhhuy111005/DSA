def bai_5():
    print("\n--- Bài 5. Nhóm theo khóa (group by) ---")
    words = ["apple", "banana", "apricot", "cherry", "blueberry"]
    print(f"Danh sách từ: {words}")

    grouped = {}
    for word in words:
        key = word[0]  # Nhóm theo chữ cái đầu
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(word)

    print(f"Kết quả nhóm theo chữ cái đầu: {grouped}")
