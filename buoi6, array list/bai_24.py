def bai_24():
    print("\n--- Bài 24 (Bài 9 LL): Trộn hai danh sách đã sắp xếp ---")

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

    h1 = Node(1)
    h1.next = Node(3)
    h1.next.next = Node(5)

    h2 = Node(2)
    h2.next = Node(4)

    dummy = Node(0)
    tail = dummy

    while h1 and h2:
        if h1.data < h2.data:
            tail.next = h1
            h1 = h1.next
        else:
            tail.next = h2
            h2 = h2.next
        tail = tail.next

    tail.next = h1 if h1 else h2

    print("Kết quả trộn liên kết sắp xếp: ", end="")
    print_singly_list(dummy.next)
