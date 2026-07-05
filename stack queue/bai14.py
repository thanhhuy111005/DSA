# Bài 14. Bài toán nhịp giá cổ phiếu (Stock Span) [cite: 44, 45]
def bai14(prices):
    span = []
    stack = []
    for i in range(len(prices)):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        span.append(i + 1 if not stack else i - stack[-1])
        stack.append(i)
    return span

