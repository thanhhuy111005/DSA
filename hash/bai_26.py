def bai_26():
    print("\n--- Bài 26 (Bài 11 HF): Hàm băm độc lập thứ tự ---")

    def order_independent_hash(elements):
        hash_sum = 0
        for item in elements:
            # Sử dụng toán tử XOR hoặc Cộng để triệt tiêu phụ thuộc thứ tự
            hash_sum += hash(item)
        return hash_sum

    set1 = [1, 2, 3]
    set2 = [3, 1, 2]
    print(f"Tập 1: {set1} | Tập 2: {set2}")
    print(f"Hash tập 1: {order_independent_hash(set1)}")
    print(f"Hash tập 2: {order_independent_hash(set2)}")
