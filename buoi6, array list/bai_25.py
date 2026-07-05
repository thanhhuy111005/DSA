def bai_25():
    print("\n--- Bài 25 (Bài 10 LL): Xóa nút thứ k từ cuối ---")

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

    def print_singly_list(head):
        curr = head
        nodes = []
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next
        nodes.append("null")
        print(" -> ".join(nodes))

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    k = 2
    print("Danh sách ban đầu: ", end="")
    print_singly_list(head)

    dummy = Node(0)
    dummy.next = head
    fast = slow = dummy

    for _ in range(k):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    print(f"Danh sách sau khi xóa nút thứ {k} từ cuối lên: ", end="")
    print_singly_list(dummy.next)
