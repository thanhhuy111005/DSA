# Bài 27. Bài toán Josephus [cite: 91, 92]
def bai27(n, k):
    q = deque(range(1, n + 1))
    while len(q) > 1:
        for _ in range(k - 1): q.append(q.popleft())
        q.popleft()
    return q[0]

