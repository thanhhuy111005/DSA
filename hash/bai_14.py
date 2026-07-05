def bai_14():
    print("\n--- Bài 14. Xóa lười trong open addressing ---")

    class LazyDeleteHashTable:

        def __init__(self, capacity=10):
            self.capacity = capacity
            self.keys = [None] * self.capacity
            self.vals = [None] * self.capacity
            self.DELETED = "<tombstone_deleted_marker>"

        def _hash(self, key):
            return hash(key) % self.capacity

        def put(self, key, val):
            idx = self._hash(key)
            first_deleted_idx = None
            start_idx = idx

            while self.keys[idx] is not None:
                if self.keys[idx] == key:
                    self.vals[idx] = val  # Ghi đè khóa cũ
                    return
                if self.keys[idx] == self.DELETED and first_deleted_idx is None:
                    first_deleted_idx = idx  # Lưu lại ô trống lười đầu tiên để tối ưu tái sử dụng
                idx = (idx + 1) % self.capacity
                if idx == start_idx:
                    break

            insert_idx = (
                first_deleted_idx if first_deleted_idx is not None else idx
            )
            if self.keys[insert_idx] is not None and self.keys[insert_idx] != self.DELETED:
                raise MemoryError("Bảng đầy!")

            self.keys[insert_idx] = key
            self.vals[insert_idx] = val
            print(f"Đã Put khóa '{key}' vào ô chỉ số {insert_idx}")

        def remove(self, key):
            idx = self._hash(key)
            start_idx = idx
            while self.keys[idx] is not None:
                if self.keys[idx] == key:
                    self.keys[idx] = self.DELETED
                    self.vals[idx] = None
                    print(f"Đã thực hiện xóa lười (Tombstone) tại index {idx}")
                    return True
                idx = (idx + 1) % self.capacity
                if idx == start_idx:
                    break
            return False

    ht = LazyDeleteHashTable()
    ht.put("Data1", 10)
    ht.remove("Data1")
    ht.put("Data2", 20)  # Sẽ điền vào chính ô đã xóa lười
