def bai_30():
    print("\n--- Bài 30 (Bài 15 HF): MinHash ước lượng độ tương đồng ---")

    class MinHashEstimator:

        def __init__(self, num_hashes=10):
            self.num_hashes = num_hashes
            # Khởi tạo các hàm băm ngẫu nhiên dạng (a*x + b) % p
            self.p = 1000003
            self.hash_params = [
                (random.randint(1, self.p - 1), random.randint(0, self.p - 1))
                for _ in range(self.num_hashes)
            ]

        def compute_signature(self, s_set):
            signature = [float("inf")] * self.num_hashes
            for element in s_set:
                element_hash_base = hash(element)
                for i, (a, b) in enumerate(self.hash_params):
                    hash_val = ((a * element_hash_base + b) % self.p)
                    if hash_val < signature[i]:
                        signature[i] = hash_val
            return signature

        def estimate_jaccard(self, sig1, sig2):
            # Tính tỷ lệ các vị trí ký hiệu trùng nhau giữa hai chữ ký thành phần
            matches = sum(1 for i, j in zip(sig1, sig2) if i == j)
            return matches / self.num_hashes

    set_a = {"apple", "banana", "cherry"}
    set_b = {"banana", "cherry", "dragonfruit"}

    estimator = MinHashEstimator(num_hashes=20)
    sig_a = estimator.compute_signature(set_a)
    sig_b = estimator.compute_signature(set_b)

    actual_jaccard = len(set_a.intersection(set_b)) / len(set_a.union(set_b))
    estimated_jaccard = estimator.estimate_jaccard(sig_a, sig_b)

    print(f"Độ tương đồng Jaccard thực tế: {actual_jaccard:.2f}")
    print(f"Độ tương đồng ước lượng bằng MinHash: {estimated_jaccard:.2f}")


# ==========================================
# KHỐI ĐIỀU KHIỂN MENU CHẠY CHƯƠNG TRÌNH
# ==========================================
