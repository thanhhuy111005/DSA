def bai_19():
    print("\n--- Bài 19 (Bài 4 LL): Chèn sau một nút cho trước ---")

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
    head.next = Node(3)
    print("Danh sách gốc: ", end="")
    print_singly_list(head)

    target_node = head
    new_node = Node(2)
    new_node.next = target_node.next
    target_node.next = new_node

    print("Danh sách sau khi chèn nút 2 sau nút 1: ", end="")
    print_singly_list(head)
