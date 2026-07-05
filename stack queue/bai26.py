# Bài 26. Giá trị lớn nhất trong cửa sổ trượt [cite: 88, 89]
def bai26(arr, k):
    q = deque()
    res = []
    for i, x in enumerate(arr):
        while q and arr[q[-1]] <= x: q.pop()
        q.append(i)
        if q[0] == i - k: q.popleft()
        if i >= k - 1: res.append(arr[q[0]])
    return res

