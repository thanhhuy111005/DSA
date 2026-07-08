def bai_1():
    print("\n--- Bài 1: Cài đặt Array List cơ bản ---")

    class ArrayListCơBản:

        def __init__(self):
            self.data = []

        def add(self, x):
            self.data.append(x)
            print(f"Add {x} -> Danh sách: {self.data}")

        def get(self, index):
            return (
                self.data[index] if 0 <= index < len(self.data) else "Lỗi index"
            )

        def set(self, index, val):
            if 0 <= index < len(self.data):
                self.data[index] = val
                print(
                    f"Set vị trí {index} thành {val} -> Danh sách: {self.data}"
                )
            else:
                print("Lỗi index")

        def size(self):
            return len(self.data)

    arr = ArrayListCơBản()
    arr.add(1)
    arr.add(2)
    arr.add(3)
    print(f"get(1) = {arr.get(1)}")
    arr.set(1, 9)
