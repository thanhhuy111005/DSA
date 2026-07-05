def bai_20():
    print("\n--- Bài 20 (Bài 5 LL): Xóa nút theo giá trị ---")

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
    head.next.next.next = Node(2)
    print("Danh sách gốc: ", end="")
    print_singly_list(head)

    def remove_first_match(head_ref, x):
        curr = head_ref
        prev = None
        if curr and curr.data == x:
            return curr.next
        while curr and curr.data != x:
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next
        return head_ref

    head = remove_first_match(head, 2)
    print("Danh sách sau khi xóa nút đầu tiên có giá trị 2: ", end="")
    print_singly_list(head)
