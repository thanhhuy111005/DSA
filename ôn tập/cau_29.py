def cau_29():
    print("\n--- Câu 29. Giá trị lớn nhất trong cửa sổ trượt ---")

    def max_sliding_window(arr, k):
        q = deque()  # Lưu chỉ số phần tử đơn điệu giảm dần
        res = []
        for i, num in enumerate(arr):
            # Loại bỏ phần tử đã lọt thỏm ra ngoài cửa sổ trượt phía trước
            if q and q[0] < i - k + 1:
                q.popleft()
            # Duy trì tính giảm đơn điệu bằng cách xả các phần tử nhỏ hơn num
            while q and arr[q[-1]] < num:
                q.pop()
            q.append(i)
            # Lưu lại giá trị lớn nhất khi cửa sổ đã đạt đủ độ dài k
            if i >= k - 1:
                res.append(arr[q[0]])
        return res

    a = [1, 3, -1, -1, 5, 3]
    k = 3
    print(f"Mảng: {a}, Cửa sổ k = {k} -> Dãy cực đại trượt: {max_sliding_window(a, k)}")
