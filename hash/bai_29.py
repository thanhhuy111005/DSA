def bai_29():
    print("\n--- Bài 29 (Bài 14 HF): Bloom Filter ---")

    class SimpleBloomFilter:

        def __init__(self, size=1000, num_hashes=3):
            self.size = size
            self.num_hashes = num_hashes
            self.bit_array = [0] * self.size

        def _get_hashes(self, item):
            hashes = []
            # Sinh ra k chỉ số vị trí bit khác nhau bằng cách kết hợp chuỗi thêm gia vị hạt giống
            for i in range(self.num_hashes):
                encoded = f"{item}-{i}".encode("utf-8")
                hash_val = (
                    int(hashlib.sha256(encoded).hexdigest(), 16) % self.size
                )
                hashes.append(hash_val)
            return hashes

        def add(self, item):
            for bit_idx in self._get_hashes(item):
                self.bit_array[bit_idx] = 1

        def contains(self, item):
            for bit_idx in self._get_hashes(item):
                if self.bit_array[bit_idx] == 0:
                    return False  # Khẳng định 100% không tồn tại
            return True  # Xác suất cao là có tồn tại (có thể dính dương tính giả)

    bf = SimpleBloomFilter()
    bf.add("apple")
    bf.add("banana")
    print(f"Kiểm tra 'apple' -> {bf.contains('apple')}")
    print(f"Kiểm tra 'cherry' -> {bf.contains('cherry')}")
