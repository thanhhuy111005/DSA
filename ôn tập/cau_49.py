def cau_49():
    print("\n--- Câu 49. Universal hashing ---")

    class UniversalHash:

        def __init__(self, m=10, p=1000003):
            self.m, self.p = m, p
            self.a = random.randint(1, p - 1)
            self.b = random.randint(0, p - 1)  # Chọn ngẫu nhiên khi tạo bảng

        def hash(self, k):
            return ((self.a * k + self.b) % self.p) % self.m

    uh = UniversalHash()
    print(f"Hàm băm phổ quát được sinh ngẫu nhiên thành công. Mã băm số 99 = {uh.hash(99)}")
    print("Ưu điểm: Do các tham số được chọn ngẫu nhiên lúc runtime, kẻ tấn công không thể")
    print("biết trước để cố ý thiết kế các tập dữ liệu xấu gây nghẽn (hash flooding).")
