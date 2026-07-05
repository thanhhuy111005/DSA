# Bài 22. Đảo ngược hàng đợi [cite: 76, 77]
def bai22(q):
    stack = []
    while q: stack.append(q.popleft())
    while stack: q.append(stack.pop())
    return q

