# Bài 9. Chuyển trung tố sang hậu tố [cite: 27, 28]
def bai9(expression):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    output = []
    stack = []
    for char in expression:
        if char.isalnum(): output.append(char)
        elif char == '(': stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(': output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(char, 0):
                output.append(stack.pop())
            stack.append(char)
    while stack: output.append(stack.pop())
    return "".join(output)

