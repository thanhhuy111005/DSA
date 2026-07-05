def bai_7():
    print("\n--- Bài 7. Hệ số tải và rehashing ---")

    class RehashHashTable:

        def __init__(self, capacity=4):
            self.capacity = capacity
            self.size = 0
            self.buckets = [[] for _ in range(self.capacity)]

        def _hash(self, key, cap):
            return hash(key) % cap

        def put(self, key, val):
            # Kiểm tra cập nhật giá trị trước
            idx = self._hash(key, self.capacity)
            for pair in self.buckets[idx]:
                if pair[0] == key:
                    pair[1] = val
                    return

            # Thêm mới
            self.buckets[idx].append([key, val])
            self.size += 1

            # Kiểm tra hệ số tải vượt ngưỡng 0.75
            if self.size / self.capacity > 0.75:
                print(
                    f"-> Hệ số tải = {self.size/self.capacity:.2f} (>0.75). Tiến hành Rehash!"
                )
                self._rehash()

        def _rehash(self):
            old_buckets = self.buckets
            self.capacity *= 2
            self.buckets = [[] for _ in range(self.capacity)]
            self.size = 0
            for bucket in old_buckets:
                for key, val in bucket:
                    self.put(key, val)
            print(f"   Dung lượng mới sau khi nâng cấp: {self.capacity}")

        def get(self, key):
            idx = self._hash(key, self.capacity)
            for pair in self.buckets[idx]:
                if pair[0] == key:
                    return pair[1]
            return None

    ht = RehashHashTable()
    for i in range(5):
        ht.put(f"Key{i}", i)
