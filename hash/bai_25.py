def bai_25():
    print("\n--- Bài 25 (Bài 10 HF): Phương pháp nhân (multiplication method) ---")

    def multiplication_hash(k, m=1024):
        # Hằng số tỉ lệ vàng A xấp xỉ 0.6180339887
        A = (math.sqrt(5) - 1) / 2
        fractional_part = (k * A) % 1
        return math.floor(m * fractional_part)

    print(f"Kích thước bảng m = 1024 (lũy thừa 2 thuận tiện cho máy tính)")
    print(f"Mã băm nhân của số khóa 123456: {multiplication_hash(123456)}")
