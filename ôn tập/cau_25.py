def cau_25():
    print("\n--- Câu 25. Histogram lớn nhất ---")

    def largest_rectangle_area(heights):
        stack = []  # Lưu chỉ số thanh chiều cao
        max_area = 0
        heights.append(0)  # Thêm phần tử lính canh để kích hoạt xả hết stack cuối cùng

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else (i - stack[-1] - 1)
                max_area = max(max_area, height * width)
            stack.append(i)

        heights.pop()  # Khôi phục trạng thái mảng cũ
        return max_area

    h = [2, 1, 5, 6, 2, 3]
    print(f"Histogram Heights: {h} -> Diện tích HCN lớn nhất: {largest_rectangle_area(h)}")


# ==============================================================================
# 5. HÀNG ĐỢI (QUEUE - FIFO)
# ==============================================================================
