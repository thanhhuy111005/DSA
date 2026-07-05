def cau_23():
    print("\n--- Câu 23. Tính biểu thức hậu tố (RPN) ---")

    def eval_rpn(expression):
        stack = []
        tokens = expression.split()
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]

    expr = "3 4 + 2 * 1 -"  # Tương đương: ((3+4)*2) - 1
    print(f"Biểu thức hậu tố RPN: '{expr}' -> Giá trị tính được: {eval_rpn(expr)}")
