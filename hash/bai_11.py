def bai_11():
    print("\n--- Bài 11. Cài đặt HashSet ---")

    class SimpleHashSet:

        def __init__(self):
            self.map = {}

        def add(self, key):
            self.map[key] = True

        def contains(self, key):
            return key in self.map

        def remove(self, key):
            if key in self.map:
                del self.map[key]
                return True
            return False

        def get_elements(self):
            return list(self.map.keys())

    s_set = SimpleHashSet()
    s_set.add(1)
    s_set.add(1)
    s_set.add(2)
    print(f"Sau khi add(1, 1, 2) -> HashSet hiện tại: {s_set.get_elements()}")
    print(f"Kiểm tra xem tập hợp chứa 2 không? -> {s_set.contains(2)}")
