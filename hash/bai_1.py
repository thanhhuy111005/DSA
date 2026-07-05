def bai_1():
    print("\n--- Bài 1. Cài đặt bảng băm bằng chaining ---")

    class Node:

        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None

    class ChainingHashTable:

        def __init__(self, capacity=10):
            self.capacity = capacity
            self.buckets = [None] * self.capacity

        def _hash(self, key):
            return hash(key) % self.capacity

        def put(self, key, val):
            idx = self._hash(key)
            if not self.buckets[idx]:
                self.buckets[idx] = Node(key, val)
                return
            curr = self.buckets[idx]
            while curr:
                if curr.key == key:
                    curr.val = val
                    return
                if not curr.next:
                    break
                curr = curr.next
            curr.next = Node(key, val)

        def get(self, key):
            idx = self._hash(key)
            curr = self.buckets[idx]
            while curr:
                if curr.key == key:
                    return curr.val
                curr = curr.next
            return None

        def remove(self, key):
            idx = self._hash(key)
            curr = self.buckets[idx]
            prev = None
            while curr:
                if curr.key == key:
                    if prev:
                        prev.next = curr.next
                    else:
                        self.buckets[idx] = curr.next
                    return True
                prev = curr
                curr = curr.next
            return False

    ht = ChainingHashTable()
    ht.put("a", 1)
    print(f"put('a', 1) -> get('a') = {ht.get('a')}")
    ht.remove("a")
    print(f"Sau khi remove('a') -> get('a') = {ht.get('a')}")
