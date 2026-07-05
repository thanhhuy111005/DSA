def bai_30():
    print("\n--- Bài 30 (Bài 15 LL): LRU Cache ---")

    class DoublyNode:

        def __init__(self, key=0, val=0):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    class LRUCache:

        def __init__(self, capacity):
            self.capacity = capacity
            self.hash_map = {}
            self.head = DoublyNode(0, 0)
            self.tail = DoublyNode(0, 0)
            self.head.next = self.tail
            self.tail.prev = self.head

        def _remove(self, node):
            p = node.prev
            n = node.next
            p.next = n
            n.prev = p

        def _add_to_head(self, node):
            node.next = self.head.next
            node.next.prev = node
            self.head.next = node
            node.prev = self.head

        def get(self, key):
            if key in self.hash_map:
                node = self.hash_map[key]
                self._remove(node)
                self._add_to_head(node)
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
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.hash_map[lru_node.key]
                print(
                    f"-> Thùng cache đầy, đã loại bỏ khóa ít dùng nhất: {lru_node.key}"
                )

    cache = LRUCache(2)
    cache.put(1, "Data A")
    cache.put(2, "Data B")
    print(f"Lấy khóa 1: {cache.get(1)}")
    cache.put(3, "Data C")  # Tràn cache, đẩy khóa 2 đi


# ==========================================
# KHỐI ĐIỀU KHIỂN MENU CHẠY CHƯƠNG TRÌNH
# ==========================================
