def bai_3():
    print("\n--- Bài 3. Đếm tần suất ---")
    arr = ["a", "b", "a", "c", "a"]
    print(f"Mảng ban đầu: {arr}")

    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1

    print(f"Kết quả đếm tần suất: {freq}")
