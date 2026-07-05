# Bài 16. Cài đặt hàng đợi cơ bản [cite: 54, 55]
class bai16:
    def __init__(self):
        self.queue = deque()
    def enqueue(self, x):
        self.queue.append(x)
    def dequeue(self):
        if not self.is_empty(): return self.queue.popleft()
        return "Underflow"
    def front(self):
        return self.queue[0] if not self.is_empty() else None
    def is_empty(self):
        return len(self.queue) == 0

