def cau_35():
    print("\n--- Câu 35. Merge Intervals ---")
    intervals = [[1, 3], [2, 6], [8, 10]]
    print(f"Các khoảng gốc: {intervals}")

    intervals.sort(key=lambda x: x[0])  # Sắp xếp theo điểm bắt đầu
    merged = []
    for item in intervals:
        if not merged or merged[-1][1] < item[0]:
            merged.append(item)
        else:
            merged[-1][1] = max(merged[-1][1], item[1])

    print(f"Các khoảng sau khi gộp giao nhau: {merged}")


# ==============================================================================
# 7. LINKED LIST & QUẢN LÝ CON TRỎ PHÂN TÁN
# ==============================================================================
