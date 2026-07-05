def bai_10():
    print("\n--- Bài 10: Trộn hai danh sách đã sắp xếp ---")
    l1 = [1, 3, 5]
    l2 = [2, 4]
    print(f"Danh sách 1: {l1} | Danh sách 2: {l2}")

    merged = []
    i = j = 0
    # Dùng 2 con trỏ chạy song song để so sánh
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1

    # Gom các phần tử còn dư thừa
    merged.extend(l1[i:])
    merged.extend(l2[j:])
    print(f"Kết quả trộn sắp xếp: {merged}")
