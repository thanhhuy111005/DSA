# Bài 21. Cài đặt hàng đợi bằng hai ngăn xếp [cite: 73, 74]
class bai21:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    def enqueue(self, x):
        self.in_stack.append(x)
    def dequeue(self):
        if not self.out_stack:
            while self.in_stack: self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop() if self.out_stack else "Underflow"

