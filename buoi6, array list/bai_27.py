def bai_27():
    print("\n--- Bài 27 (Bài 12 LL): Tìm điểm bắt đầu chu trình ---")

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

    head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    head.next = node2
    node2.next = node3
    node3.next = node2

    slow = fast = head
    intersect = None
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            intersect = slow
            break

    if intersect:
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        print(f"Nút bắt đầu của chu trình khép kín có giá trị là: {ptr1.data}")
    else:
        print("Không có chu trình.")
