def bai_15():
    print("\n--- Bài 15. Băm nhất quán (Consistent Hashing) ---")

    class ConsistentHashRing:

        def __init__(self, replicas=3):
            self.replicas = replicas  # Số lượng nút ảo cho mỗi server
            self.ring = {}  # Map: Vị trí băm trên vòng -> Server thực tế
            self.sorted_keys = []

        def _hash(self, key):
            # Tạo giá trị băm nguyên dương từ chuỗi md5 để phân phối đều trên vòng tròn
            return (
                int(hashlib.md5(key.encode("utf-8")).hexdigest(), 16)
                % 1000000
            )

        def add_server(self, server):
            for i in range(self.replicas):
                virtual_node_key = f"{server}-vnode-{i}"
                val_hash = self._hash(virtual_node_key)
                self.ring[val_hash] = server
                self.sorted_keys.append(val_hash)
            self.sorted_keys.sort()
            print(f"Đã thêm Server '{server}' cùng các nút ảo vào vòng băm.")

        def remove_server(self, server):
            for i in range(self.replicas):
                virtual_node_key = f"{server}-vnode-{i}"
                val_hash = self._hash(virtual_node_key)
                if val_hash in self.ring:
                    del self.ring[val_hash]
                    self.sorted_keys.remove(val_hash)
            print(f"Đã gỡ Server '{server}' ra khỏi hệ thống.")

        def get_server(self, key):
            if not self.ring:
                return None
            val_hash = self._hash(key)
            # Tìm kiếm nhị phân ô server đầu tiên có vị trí >= val_hash
            low, high = 0, len(self.sorted_keys) - 1
            idx = 0
            if val_hash > self.sorted_keys[high]:
                idx = 0  # Vòng tròn khép kín nối ngược về phần tử đầu
            else:
                while low <= high:
                    mid = (low + high) // 2
                    if self.sorted_keys[mid] >= val_hash:
                        idx = mid
                        high = mid - 1
                    else:
                        low = mid + 1
            return self.ring[self.sorted_keys[idx]]

    ring = ConsistentHashRing()
    ring.add_server("ServerA")
    ring.add_server("ServerB")
    print(f"Khóa 'user_102' được điều phối tới: {ring.get_server('user_102')}")


# ==========================================
# PHẦN B – HÀM BĂM (HASH FUNCTION) - 15 BÀI
# ==========================================
