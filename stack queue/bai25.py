# Bài 25. Hàng đợi ưu tiên cơ bản [cite: 84, 85]
import heapq
class bai25:
    def __init__(self):
        self.heap = []
    def push(self, item, priority): # Nhỏ nhất ra trước
        heapq.heappush(self.heap, (priority, item))
    def pop(self):
        return heapq.heappop(self.heap)[1] if self.heap else "Underflow"

