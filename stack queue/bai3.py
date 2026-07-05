# Bài 3. Mô phỏng dãy thao tác [cite: 10, 11]
def bai3(commands):
    stack = []
    results = []
    for cmd in commands:
        if cmd.startswith("push"):
            val = int(cmd.split()[1])
            stack.append(val)
        elif cmd == "pop":
            if stack: results.append(f"In {stack.pop()}")
            else: results.append("Lỗi: Stack rỗng")
    return results, stack

