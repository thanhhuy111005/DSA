def bai_23():
    print("\n--- Bài 23 (Bài 8 HF): So sánh chất lượng phân bố ---")
    keys = [f"User_{i}" for i in range(1000)]
    m = 10

    # Hai hàm băm cần thử nghiệm so sánh
    def h1(s):
        return sum(ord(c) for c in s) % m

    def h2(s):
        val = 0
        for c in s:
            val = (val * 31 + ord(c)) % 1000003
        return val % m

    b1, b2 = [0] * m, [0] * m
    for k in keys:
        b1[h1(k)] += 1
        b2[h2(k)] += 1

    # Thống kê chi-square kiểm thử phân bố đồng đều (càng nhỏ càng đều tốt)
    expected = len(keys) / m
    chi1 = sum((count - expected) ** 2 / expected for count in b1)
    chi2 = sum((count - expected) ** 2 / expected for count in b2)

    print(f"Hàm băm 1 (Tổng mã ký tự) -> Phân bổ: {b1} | Chi-Square: {chi1:.2f}")
    print(f"Hàm băm 2 (Đa thức 31)   -> Phân bổ: {b2} | Chi-Square: {chi2:.2f}")
    print(
        f"Kết luận: Hàm băm số {'2' if chi2 < chi1 else '1'} có độ phân tán đều chuẩn hơn."
    )
