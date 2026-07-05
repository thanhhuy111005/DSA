def bai_13():
    print("\n--- Bài 13: Trộn các khoảng (Merge Intervals) ---")
    intervals = [[1, 3], [2, 6], [8, 10]]
    print(f"Các khoảng ban đầu: {intervals}")

    # Bước 1: Sắp xếp các khoảng theo điểm bắt đầu (start)
    intervals.sort(key=lambda x: x[0])

    merged = []
    for current in intervals:
        # Nếu danh sách trống hoặc khoảng hiện tại không giao với khoảng cuối cùng trong merged
        if not merged or merged[-1][1] < current[0]:
            merged.append(current)
        else:
            # Có giao nhau, tiến hành gộp khoảng bằng cách cập nhật điểm kết thúc (end) max
            merged[-1][1] = max(merged[-1][1], current[1])

    print(f"Các khoảng sau khi gộp: {merged}")
