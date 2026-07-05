def bai_27():
    print("\n--- Bài 27 (Bài 12 HF): Tấn công hash flooding ---")
    print("[Mô phỏng cơ chế thực nghiệm]:")
    print(
        "- Bản chất: Kẻ tấn công tạo ra hàng loạt chuỗi ký tự khác nhau nhưng có chung một giá trị băm."
    )
    print(
        "- Hệ quả: Khiến bảng băm bị va chạm tuyệt đối, suy biến thành danh sách liên kết đơn,"
    )
    print("           độ phức tạp tìm kiếm nhảy vọt từ O(1) lên O(n), làm quá tải CPU (DoS).")

    # Minh họa ngẫu nhiên sinh khóa va chạm ép buộc cho hàm băm đơn giản (Mod 4)
    m = 4
    collision_keys = [x for x in range(20) if x % m == 0]
    print(f"Danh sách khóa va chạm cố ý vào bucket 0: {collision_keys}")
    print(
        "Giải pháp phòng chống: Bắt buộc nhúng mã Salt bí mật ngẫu nhiên hóa khi khởi dựng bảng (như SipHash trong Python)."
    )
