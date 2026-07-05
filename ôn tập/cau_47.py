def cau_47():
    print("\n--- Câu 47. Polynomial rolling hash ---")

    def poly_hash(s, p=31, m=10**9 + 7):
        hash_val = 0
        for char in s:
            hash_val = (hash_val * p + ord(char)) % m
        return hash_val

    print(f"Hash của chuỗi 'abc': {poly_hash('abc')}")
    print("Vai trò cấu trúc: Hệ số p (thường chọn số nguyên tố nhỏ như 31) giúp phân biệt")
    print("thứ tự đảo chữ của ký tự, m (số nguyên tố lớn) giới hạn dải băm giảm va chạm.")
