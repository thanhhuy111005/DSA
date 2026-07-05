def bai_18():
    print("\n--- Bài 18 (Bài 3 HF): Hàm băm đa thức (polynomial) ---")

    def polynomial_rolling_hash(s, p=31, m=10**9 + 7):
        hash_val = 0
        for char in s:
            hash_val = (hash_val * p + ord(char)) % m
        return hash_val

    p, m = 31, 10**9 + 7
    str1 = "abc"
    str2 = "cba"
    print(f"Hàm băm đa thức với hệ số p={p}, m={m}:")
    print(f"Hash('{str1}') = {polynomial_rolling_hash(str1, p, m)}")
    print(f"Hash('{str2}') = {polynomial_rolling_hash(str2, p, m)}")
    print("-> Ưu điểm: Đã phân biệt được rõ ràng thứ tự xuất hiện ký tự khác nhau.")
