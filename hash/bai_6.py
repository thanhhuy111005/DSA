def bai_6():
    print("\n--- Bài 6. So sánh chaining vs open addressing ---")
    print("[Phân tích lý thuyết so sánh chuyên sâu]:")
    print(
        "- Bộ nhớ: Chaining tốn thêm bộ nhớ cho con trỏ (next pointer) tại mỗi nút."
    )
    print(
        "          Open Addressing tiết kiệm con trỏ nhưng cần mảng kích thước đủ lớn."
    )
    print(
        "- Hệ số tải cao: Chaining suy biến tuyến tính từ từ (hiệu năng giảm dần thành O(N))."
    )
    print(
        "                 Open Addressing (dò tuyến tính) suy biến rất nặng do hiện tượng gom cụm,"
    )
    print("                 khi hệ số tải tiến gần 1.0, việc tìm ô trống rất chậm.")
    print(
        "- Xóa phần tử: Chaining xóa rất dễ dàng (chỉ ngắt liên kết nút đơn giản)."
    )
    print(
        "               Open Addressing không thể xóa vật lý trực tiếp vì sẽ phá vỡ chuỗi dò tìm,"
    )
    print("               bắt buộc phải sử dụng nhãn xóa lười (Tombstone).")
