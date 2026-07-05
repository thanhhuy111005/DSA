# Bài 7. Min Stack getMin O(1) [cite: 22, 23]
class bai7:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]: self.min_stack.append(x)
    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]: self.min_stack.pop()
            return val
    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None

