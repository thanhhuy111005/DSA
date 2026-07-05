def cau_27():
    print("\n--- Câu 27. Queue bằng hai stack ---")

    class StackQueue:

        def __init__(self):
            self.in_stack = []
            self.out_stack = []  # Cặp ngăn xếp bổ trợ song song

        def enqueue(self, x):
            self.in_stack.append(x)

        def dequeue(self):
            if not self.out_stack:
                while self.in_stack:
                    self.out_stack.append(self.in_stack.pop())
            if not self.out_stack:
                return "Hàng đợi rỗng!"
            return self.out_stack.pop()

    sq = StackQueue()
    sq.enqueue(1)
    sq.enqueue(2)
    print(f"Mô phỏng Queue bằng Stack -> dequeue(): {sq.dequeue()}")
    print("Chứng minh: Mỗi phần tử đi vào in-stack và đi ra khỏi out-stack chính xác 1 lần,")
    print("do đó chi phí trung bình (Amortized Cost) đạt trạng thái O(1) tối ưu tuyệt đối.")
