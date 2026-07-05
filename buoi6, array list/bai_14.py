def bai_14():
    print("\n--- Bài 14: Mảng động 2 chiều (Ma trận động) ---")

    class DynamicMatrix:

        def __init__(self):
            self.matrix = []

        def add_row(self, row_list):
            self.matrix.append(row_list)
            print(f"Đã thêm hàng mới -> Ma trận hiện tại: {self.matrix}")

        def set(self, i, j, val):
            self.matrix[i][j] = val

        def get(self, i, j):
            return self.matrix[i][j]

    dm = DynamicMatrix()
    dm.add_row([1, 2])
    dm.add_row([3, 4])
    dm.set(0, 1, 99)
    print(f"Giá trị tại (0, 1) sau khi set: {dm.get(0, 1)}")
    print(f"Ma trận cuối cùng: {dm.matrix}")
