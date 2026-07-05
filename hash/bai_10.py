def bai_10():
    print("\n--- Bài 10. Phần tử không lặp đầu tiên ---")
    s = "leetcode"
    print(f"Chuỗi kiểm tra: '{s}'")

    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    result = None
    for char in s:
        if counts[char] == 1:
            result = char
            break

    print(f"Ký tự đầu tiên không lặp lại: '{result}'")
