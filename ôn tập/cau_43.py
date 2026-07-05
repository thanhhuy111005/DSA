def cau_43():
    print("\n--- Câu 43. Hệ số tải & rehashing ---")

    class RehashDemo:

        def __init__(self):
            self.capacity = 2
            self.size = 0
            self.buckets = [[] for _ in range(self.capacity)]

        def put(self, key, val):
            idx = hash(key) % self.capacity
            self.buckets[idx].append((key, val))
            self.size += 1

            # Khi hệ số tải (load factor) vượt ngưỡng 0.75
            if self.size / self.capacity > 0.75:
                print(f"-> Hệ số tải = {self.size/self.capacity:.2f} (>0.75). Rehash nâng cấp mảng!")
                old_buckets = self.buckets
                self.capacity *= 2  # Gấp đôi kích thước m
                self.buckets = [[] for _ in range(self.capacity)]
                self.size = 0
                for b in old_buckets:
                    for k, v in b:
                        self.put(k, v)

    rd = RehashDemo()
    rd.put("K1", 10)
    rd.put("K2", 20)  # Kích hoạt sự kiện rehash tự động mở rộng
