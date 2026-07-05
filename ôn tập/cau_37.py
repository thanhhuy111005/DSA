def cau_37():
    print("\n--- Câu 37. Tìm nút giữa ---")

    class Node:

        def __init__(self, val=0):
            self.val = val
            self.next = None

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # Kỹ thuật con trỏ Nhanh/Chậm (Slow/Fast pointer)
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    print(f"Giá trị nút nằm chính giữa danh sách chuỗi: {slow.val}")
