def cau_41():
    print("\n--- Câu 41. LRU Cache ---")

    class DoublyNode:

        def __init__(self, key=0, val=0):
            self.key = key
            self.val = val
            self.prev = self.next = None

    class LRUCache:

        def __init__(self, capacity):
            self.capacity = capacity
            self.hash_map = {}  # Bảng băm tra nhanh O(1)
            self.head = DoublyNode()
            self.tail = DoublyNode()
            self.head.next = self.tail
            self.tail.prev = self.head

        def _remove(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev

        def _add_to_head(self, node):
            node.next = self.head.next
            node.next.prev = node
            self.head.next = node
            node.prev = self.head

        def get(self, key):
            if key in self.hash_map:
                node = self.hash_map[key]
                self._remove(node)
                self._add_to_head(node)  # Đẩy lên đầu ưu tiên do vừa tương tác
                return node.val
            return -1

        def put(self, key, value):
            if key in self.hash_map:
                self._remove(self.hash_map[key])
                del self.hash_map[key]
            node = DoublyNode(key, value)
            self._add_to_head(node)
            self.hash_map[key] = node

            if len(self.hash_map) > self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.hash_map[lru.key]  # Trục xuất phần tử cũ ít dùng nhất ở đáy

    cache = LRUCache(2)
    cache.put(1, "A")
    cache.put(2, "B")
    print(f"LRU Cache Put('A', 'B') -> Get Key 1: '{cache.get(1)}'")


# ==============================================================================
# 8. BẢNG BĂM (HASH TABLE)
# ==============================================================================
