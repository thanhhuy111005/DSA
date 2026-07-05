def bai_17():
    print("\n--- Bài 17 (Bài 2 HF): Hàm băm cho chuỗi (tổng mã ký tự) ---")

    def simple_string_hash(s, m):
        return sum(ord(c) for c in s) % m

    m = 100
    str1 = "abc"
    str2 = "cba"  # Đảo chữ của str1

    hash1 = simple_string_hash(str1, m)
    hash2 = simple_string_hash(str2, m)

    print(f"Hàm băm tổng ký tự mod {m}:")
    print(f"Hash('{str1}') = {hash1}")
    print(f"Hash('{str2}') = {hash2}")
    print("Nhược điểm chí mạng: Các chuỗi đảo chữ luôn luôn cho cùng giá trị băm!")
