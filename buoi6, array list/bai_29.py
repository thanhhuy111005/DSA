def bai_29():
    print(
        "\n--- Bài 29 (Bài 14 LL): Cộng hai số biểu diễn bằng linked list ---"
    )

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

    l1 = Node(2)
    l1.next = Node(4)
    l1.next.next = Node(3)

    l2 = Node(5)
    l2.next = Node(6)
    l2.next.next = Node(4)

    dummy = Node(0)
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.data if l1 else 0
        val2 = l2.data if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        curr.next = Node(total % 10)

        curr = curr.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    print("Kết quả phép cộng lưu ngược: ", end="")
    print_singly_list(dummy.next)
