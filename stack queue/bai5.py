# Bài 5. Duyệt và đếm phần tử [cite: 16, 17]
def bai5(stack):
    temp_stack = []
    count = 0
    elements = []
    while stack:
        val = stack.pop()
        elements.append(val)
        count += 1
        temp_stack.append(val)
    while temp_stack:
        stack.append(temp_stack.pop())
    return count, elements

