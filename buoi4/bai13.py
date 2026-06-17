def bai_13(students):
    """Sắp xếp danh sách học sinh theo điểm tăng dần bằng selection sort[cite: 44, 45]."""
    n = len(students)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if students[j][1] < students[min_idx][1]: min_idx = j
        students[i], students[min_idx] = students[min_idx], students[i]
    return students

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

