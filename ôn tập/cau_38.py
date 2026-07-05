def cau_38():
    print("\n--- Câu 38. Phát hiện & tìm đầu chu trình ---")

    class Node:

        def __init__(self, val=0):
            self.val = val
            self.next = None

    head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    head.next = node2
    node2.next = node3
    node3.next = node2  # Tạo vòng lặp khép kín tại đây

    # Giai đoạn 1: Thuật toán Floyd phát hiện chu trình
    slow = fast = head
    intersect = None
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            intersect = slow
            break

    # Giai đoạn 2: Tìm nút gốc bắt đầu của chu trình
    if intersect:
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        print(f"Nút bắt đầu của chu trình khép kín có giá trị = {ptr1.val}")
