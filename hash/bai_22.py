def bai_22():
    print("\n--- Bài 22 (Bài 7 HF): Hàm băm cho cặp / tuple ---")

    def hash_combine(seed, v):
        # Mô phỏng thuật toán kết hợp phân tán bit của thư viện chuẩn Boost (C++)
        return seed ^ (hash(v) + 0x9E3779B9 + (seed << 6) + (seed >> 2))

    def hash_tuple(tup):
        result_seed = 0
        for item in tup:
            result_seed = hash_combine(result_seed, item)
        return result_seed

    pair1 = (10, 20)
    pair2 = (20, 10)
    print(f"Hash của tuple {pair1}: {hash_tuple(pair1)}")
    print(f"Hash của tuple {pair2}: {hash_tuple(pair2)}")
