def cau_42():
    print("\n--- Câu 42. Chaining & open addressing ---")
    print("[Hệ thống kiến thức so sánh đối chiếu cốt lõi]:")
    print("- Separate Chaining: Mỗi ô chứa một danh sách liên kết lưu các phần tử va chạm.")
    print("                    Không lo bảng bị đầy, hiệu năng giảm tuyến tính dịu nhẹ khi tải cao.")
    print("- Linear Probing (Địa chỉ mở): Khi va chạm, tìm kiếm tuyến tính ô trống kế tiếp.")
    print("                             Bảng có thể bị đầy, dễ dính lỗi gom cụm giảm tốc độ cực nặng.")
