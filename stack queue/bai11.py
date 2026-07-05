# Bài 11. Phần tử lớn hơn kế tiếp (Next Greater Element) [cite: 34, 35]
def bai11(arr):
    res = [-1] * len(arr)
    stack = []
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            res[stack.pop()] = arr[i]
        stack.append(i)
    return res

