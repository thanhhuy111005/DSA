def cau_26():
    print("\n--- Câu 26. Hàng đợi vòng ---")

    class CircularQueue:

        def __init__(self, k):
            self.k = k
            self.queue = [None] * k
            self.head = self.tail = -1

        def enqueue(self, value):
            if (self.tail + 1) % self.k == self.head:
                return "Hàng đợi đầy!"
            elif self.head == -1:
                self.head = self.tail = 0
                self.queue[self.tail] = value
            else:
                self.tail = (self.tail + 1) % self.k
                self.queue[self.tail] = value
            return True

        def dequeue(self):
            if self.head == -1:
                return "Hàng đợi rỗng"
            res = self.queue[self.head]
            if self.head == self.tail:
                self.head = self.tail = -1
            else:
                self.head = (self.head + 1) % self.k
            return res

    cq = CircularQueue(3)
    cq.enqueue(10)
    cq.enqueue(20)
    print(f"Dequeue hàng đợi vòng lấy ra phần tử đầu: {cq.dequeue()}")
