def bai_22():
    print("\n--- Bài 22 (Bài 7 LL): Tìm nút giữa ---")

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
    print("Danh sách: ", end="")
    print_singly_list(head)

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    print(f"Giá trị nút nằm chính giữa danh sách là: {slow.data}")
