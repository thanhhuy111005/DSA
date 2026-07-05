# Bài 2. Đảo ngược chuỗi dùng ngăn xếp [cite: 7, 8]
def bai2(s):
    stack = list(s)
    reversed_s = ""
    while stack:
        reversed_s += stack.pop()
    return reversed_s

