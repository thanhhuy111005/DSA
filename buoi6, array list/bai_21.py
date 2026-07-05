def bai_21():
    print("\n--- Bài 21 (Bài 6 LL): Đảo ngược danh sách liên kết ---")

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
    print("Danh sách gốc: ", end="")
    print_singly_list(head)

    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    head = prev

    print("Danh sách sau khi đảo ngược (vòng lặp): ", end="")
    print_singly_list(head)
