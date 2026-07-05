# Bài 29. Trung bình trượt / đếm hit trong cửa sổ thời gian [cite: 99, 100]
class bai29:
    def __init__(self, time_window=300):
        self.window = time_window
        self.hits = deque()
    def hit(self, timestamp):
        self.hits.append(timestamp)
        self.evict_expired(timestamp)
    def get_hits(self, current_time):
        self.evict_expired(current_time)
        return len(self.hits)
    def evict_expired(self, current_time):
        while self.hits and self.hits[0] <= current_time - self.window:
            self.hits.popleft()

