# Bài 10. Cài đặt ngăn xếp bằng hai hàng đợi [cite: 30, 31]
from collections import deque
class bai10:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    def push(self, x): # O(n) cost
        self.q2.append(x)
        while self.q1: self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
    def pop(self): # O(1) cost
        return self.q1.popleft() if self.q1 else "Underflow"

