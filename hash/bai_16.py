def bai_16():
    print("\n--- Bài 16 (Bài 1 HF): Hàm băm modulo cho số nguyên ---")
    keys = [12, 22, 32, 45, 57, 92]
    m = 10
    print(f"Tập khóa: {keys}, Kích thước m = {m}")

    distribution = [[] for _ in range(m)]
    for k in keys:
        idx = k % m
        distribution[idx].append(k)

    for idx, bucket in enumerate(distribution):
        print(f"Bucket {idx}: {bucket}")
