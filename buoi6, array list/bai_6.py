def bai_6():
    print("\n--- Bài 6: Tự động mở rộng dung lượng (Resizing) ---")

    class DynamicArrayMock:

        def __init__(self):
            self.capacity = 4
            self.size = 0
            self.array = [None] * self.capacity

        def append(self, x):
            if self.size == self.capacity:
                print(f"-> Mảng đầy (size={self.size}, cap={self.capacity})...")
                self.capacity *= 2
                new_array = [None] * self.capacity
                for i in range(self.size):
                    new_array[i] = self.array[i]
                self.array = new_array
                print(
                    f"   Đã cấp phát bộ nhớ mới gấp đôi! Dung lượng mới = {self.capacity}"
                )

            self.array[self.size] = x
            self.size += 1
            print(
                f"Thêm {x} thành công. Mảng thực tế trong bộ nhớ: {self.array}"
            )

    da = DynamicArrayMock()
    for item in [10, 20, 30, 40, 50]:
        da.append(item)
