def bai_2():
    print("\n--- Bài 2. Cài đặt bảng băm bằng dò tuyến tính ---")

    class LinearProbingHashTable:

        def __init__(self, capacity=10):
            self.capacity = capacity
            self.keys = [None] * self.capacity
            self.vals = [None] * self.capacity

        def _hash(self, key):
            return hash(key) % self.capacity

        def put(self, key, val):
            idx = self._hash(key)
            start_idx = idx
            while self.keys[idx] is not None:
                if self.keys[idx] == key:
                    self.vals[idx] = val
                    return
                idx = (idx + 1) % self.capacity
                if idx == start_idx:
                    raise MemoryError("Bảng băm đã đầy!")
            self.keys[idx] = key
            self.vals[idx] = val

        def get(self, key):
            idx = self._hash(key)
            start_idx = idx
            while self.keys[idx] is not None:
                if self.keys[idx] == key:
                    return self.vals[idx]
                idx = (idx + 1) % self.capacity
                if idx == start_idx:
                    break
            return None

    ht = LinearProbingHashTable()
    ht.put("x", 100)
    ht.put("y", 200)
    print(f"get('x') = {ht.get('x')}")
    print(f"get('y') = {ht.get('y')}")
