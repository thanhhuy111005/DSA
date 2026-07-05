# Bài 4. Phát hiện underflow / overflow [cite: 13, 14]
class bai4:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
    def push(self, x):
        if len(self.stack) >= self.capacity: return "Overflow"
        self.stack.append(x)
    def pop(self):
        if not self.stack: return "Underflow"
        return self.stack.pop()

