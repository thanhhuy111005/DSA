def bai_24():
    print("\n--- Bài 24 (Bài 9 HF): Băm phổ quát (Universal Hashing) ---")

    class UniversalHashFamily:

        def __init__(self, m=10, p=1000003):
            self.m = m
            self.p = p
            # Sinh ngẫu nhiên bộ tham số gia vị chống tấn công cố ý đầu vào xấu
            self.a = random.randint(1, p - 1)
            self.b = random.randint(0, p - 1)

        def hash(self, k):
            return (((self.a * k + self.b) % self.p) % self.m)

    hash_fam = UniversalHashFamily()
    print(f"Khởi tạo ngẫu nhiên thành công: a = {hash_fam.a}, b = {hash_fam.b}")
    print(f"Mã băm của số 42: {hash_fam.hash(42)}")
