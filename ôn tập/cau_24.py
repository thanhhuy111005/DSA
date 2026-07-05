def cau_24():
    print("\n--- Câu 24. Next Greater Element ---")

    def next_greater_element(arr):
        n = len(arr)
        res = [-1] * n
        stack = []  # Lưu các chỉ số tăng đơn điệu

        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                idx = stack.pop()
                res[idx] = arr[i]
            stack.append(i)
        return res

    a = [2, 1, 3]
    print(f"Mảng: {a} -> Next Greater Elements bên phải: {next_greater_element(a)}")
