def bai_23():
    print("\n--- Bài 23 (Bài 8 LL): Phát hiện chu trình ---")

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

    head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    head.next = node2
    node2.next = node3
    node3.next = node2  # Vòng lặp

    slow = fast = head
    has_cycle = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break

    print(f"Kết quả kiểm tra phát hiện chu trình vòng lặp: {has_cycle}")
