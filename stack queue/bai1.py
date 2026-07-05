# Bài 1. Cài đặt ngăn xếp bằng mảng [cite: 3, 4]
class bai1:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        if not self.is_empty(): return self.stack.pop()
        return "Underflow"
    def top(self):
        if not self.is_empty(): return self.stack[-1]
        return None
    def is_empty(self):
        return len(self.stack) == 0

