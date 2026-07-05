def bai_8():
    print("\n--- Bài 8. Quadratic probing / double hashing ---")

    class DoubleHashingTable:

        def __init__(self, capacity=11):  # Nên chọn kích thước nguyên tố
            self.capacity = capacity
            self.keys = [None] * self.capacity
            self.vals = [None] * self.capacity

        def _hash1(self, key):
            return hash(key) % self.capacity

        def _hash2(self, key):
            # Hàm băm thứ hai phải trả về số nguyên dương > 0 và nguyên tố cùng nhau với capacity
            return 7 - (hash(key) % 7)

        def put(self, key, val):
            idx = self._hash1(key)
            step = self._hash2(key)
            start_idx = idx

            while self.keys[idx] is not None:
                if self.keys[idx] == key:
                    self.vals[idx] = val
                    return
                idx = (idx + step) % self.capacity
                if idx == start_idx:
                    raise MemoryError("Bảng đầy!")

            self.keys[idx] = key
            self.vals[idx] = val
            print(
                f"Put({key}) tại index {idx} thành công bằng bước nhảy dò {step}."
            )

    ht = DoubleHashingTable()
    ht.put("Alpha", 1)
    ht.put("Beta", 2)
