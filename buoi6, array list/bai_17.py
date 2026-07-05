def bai_17():
    print("\n--- Bài 17 (Bài 2 LL): Tính độ dài / duyệt ---")

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    print("Duyệt danh sách liên kết: ")
    curr = head
    length = 0
    while curr:
        print(f"Nút giá trị: {curr.data}")
        length += 1
        curr = curr.next
    print(f"Tổng độ dài danh sách đếm được: {length}")
