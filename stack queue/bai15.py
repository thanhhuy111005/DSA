# Bài 15. Sắp xếp một ngăn xếp [cite: 47, 49]
def bai15(stack):
    tmp_stack = []
    while stack:
        tmp = stack.pop()
        while tmp_stack and tmp_stack[-1] < tmp:
            stack.append(tmp_stack.pop())
        tmp_stack.append(tmp)
    while tmp_stack:
        stack.append(tmp_stack.pop())
    return stack


# ==========================================
# PHẦN B – HÀNG ĐỢI (QUEUE)
# ==========================================

