# Bài 19. Kiểm tra rỗng / đầy [cite: 65, 66]
class bai19:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = deque()
    def enqueue(self, x):
        if len(self.queue) >= self.capacity: return "Lỗi: Đầy (Overflow)"
        self.queue.append(x)
    def dequeue(self):
        if not self.queue: return "Lỗi: Rỗng (Underflow)"
        return self.queue.popleft()
    def size(self):
        return len(self.queue)

