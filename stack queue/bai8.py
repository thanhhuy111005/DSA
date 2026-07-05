# Bài 8. Tính biểu thức hậu tố (RPN) [cite: 25, 26]
def bai8(expression):
    stack = []
    for token in expression.split():
        if token.isdigit() or (token[1:].isdigit() and token[0] == '-'):
            stack.append(int(token))
        else:
            b, a = stack.pop(), stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(int(a / b))
    return stack[0]

