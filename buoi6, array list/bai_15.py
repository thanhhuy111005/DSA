def bai_15():
    print("\n--- Bài 15: Iterator và fail-fast ---")

    class ArrayListWithIterator:

        def __init__(self, items):
            self.data = list(items)
            self.modCount = 0  # Biến đếm số lần thay đổi cấu trúc danh sách

        def remove_at(self, index):
            self.data.pop(index)
            self.modCount += 1  # Mỗi lần xóa cấu trúc bị thay đổi

        def __iter__(self):
            # Tạo bộ lặp chứa bản sao modCount tại thời điểm bắt đầu vòng lặp
            class ArrayListIterator:

                def __init__(self, outer):
                    self.outer = outer
                    self.cursor = 0
                    self.expectedModCount = outer.modCount

                def __next__(self):
                    if self.outer.modCount != self.expectedModCount:
                        raise RuntimeError(
                            "Lỗi Fail-Fast: Danh sách bị sửa đổi cấu trúc trong lúc duyệt lặp!"
                        )
                    if self.cursor >= len(self.outer.data):
                        raise StopIteration
                    val = self.outer.data[self.cursor]
                    self.cursor += 1
                    return val

            return ArrayListIterator(self)

    my_list = ArrayListWithIterator([10, 20, 30, 40])
    print("Bắt đầu lặp và can thiệp sửa đổi giữa chừng...")
    try:
        for x in my_list:
            print(f"Đang duyệt phần tử: {x}")
            if x == 20:
                my_list.remove_at(0)  # Sửa đổi danh sách khi đang lặp
    except RuntimeError as e:
        print(f"Thông báo bắt được ngoại lệ thành công: {e}")


# ==========================================
# PHẦN B – LINKED LIST (DANH SÁCH LIÊN KẾT)
# ==========================================
