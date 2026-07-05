# Bài 18. Mô phỏng dãy thao tác [cite: 62, 63]
def bai18(commands):
    queue = deque()
    results = []
    for cmd in commands:
        if cmd.startswith("enqueue") or cmd.startswith("enq"):
            val = int(cmd.split()[1])
            queue.append(val)
        elif cmd.startswith("dequeue") or cmd == "deq":
            if queue: results.append(f"In {queue.popleft()}")
            else: results.append("Lỗi: Queue rỗng")
    return results, list(queue)

