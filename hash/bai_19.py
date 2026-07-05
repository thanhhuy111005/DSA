def bai_19():
    print("\n--- Bài 19 (Bài 4 HF): Đếm va chạm của một hàm băm ---")
    keys = ["apple", "orange", "banana", "grape", "melon", "peach", "apricot"]
    m = 5

    def mock_hash(s):
        return len(s) % m

    buckets = [0] * m
    for k in keys:
        buckets[mock_hash(k)] += 1

    total_collisions = 0
    for count in buckets:
        if count > 1:
            # Số cặp va chạm trong cùng một bucket bằng n*(n-1)/2
            total_collisions += (count * (count - 1)) // 2

    print(f"Số lượng cặp khóa va chạm đồng bucket tính được: {total_collisions}")
