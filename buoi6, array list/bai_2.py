def bai_2():
    print("\n--- Bài 2: Thêm / xóa ở cuối ---")

    class ArrayListCuoi:

        def __init__(self):
            self.data = []

        def append(self, x):
            self.data.append(x)  # O(1) trung bình
            print(f"Append {x} -> Danh sách: {self.data}")

        def popBack(self):
            if self.data:
                val = self.data.pop()  # O(1)
                print(
                    f"PopBack trả về {val} -> Danh sách còn lại: {self.data}"
                )
                return val
            print("Danh sách rỗng")
            return None

    arr = ArrayListCuoi()
    arr.append(1)
    arr.append(2)
    arr.append(3)
    arr.popBack()
