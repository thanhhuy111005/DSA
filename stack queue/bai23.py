# Bài 23. Hàng đợi hai đầu (Deque) [cite: 78, 79]
class bai23:
    def __init__(self):
        self.deque = deque()
    def pushFront(self, x): self.deque.appendleft(x)
    def pushBack(self, x): self.deque.append(x)
    def popFront(self): return self.deque.popleft() if self.deque else "Underflow"
    def popBack(self): return self.deque.pop() if self.deque else "Underflow"

