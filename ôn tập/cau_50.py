def cau_50():
    print("\n--- Câu 50. Bloom filter ---")

    class BloomFilter:

        def __init__(self, size=100, num_hashes=2):
            self.size = size
            self.bit_array = [0] * size
            self.num_hashes = num_hashes

        def add(self, item):
            for i in range(self.num_hashes):
                idx = (hash(item) + i * 19) % self.size
                self.bit_array[idx] = 1

        def contains(self, item):
            for i in range(self.num_hashes):
                idx = (hash(item) + i * 19) % self.size
                if self.bit_array[idx] == 0:
                    return False  # Chắc chắn 100% không có
            return True  # Có thể có (Xác suất dính dương tính giả)

    bf = BloomFilter()
    bf.add("test")
    print(f"Kiểm tra phần tử vừa thêm 'test' -> {bf.contains('test')}")
    print("Đặc trưng: Báo 'Có' thì có thể nhầm, báo 'Không' thì tuyệt đối chính xác.")


# ==============================================================================
# KHỐI ĐIỀU KHIỂN MENU TỔNG HỢP 50 CÂU HỎI HỆ THỐNG
# ==============================================================================
