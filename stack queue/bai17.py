# Bài 17. Hàng đợi vòng (Circular Queue) [cite: 59, 60]
class bai17:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1
    def enqueue(self, value):
        if ((self.tail + 1) % self.k) == self.head: return "Overflow"
        if self.head == -1: self.head = 0
        self.tail = (self.tail + 1) % self.k
        self.queue[self.tail] = value
    def dequeue(self):
        if self.head == -1: return "Underflow"
        res = self.queue[self.head]
        if self.head == self.tail: self.head = self.tail = -1
        else: self.head = (self.head + 1) % self.k
        return res

