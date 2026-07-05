def bai_16():
    print("\n--- Bài 16 (Bài 1 LL): Cài đặt danh sách liên kết đơn ---")

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

    class SinglyLinkedList:

        def __init__(self):
            self.head = None

        def pushFront(self, data):
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

        def pushBack(self, data):
            new_node = Node(data)
            if not self.head:
                self.head = new_node
                return
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def print_singly_list(head):
        curr = head
        nodes = []
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next
        nodes.append("null")
        print(" -> ".join(nodes))

    ll = SinglyLinkedList()
    ll.pushFront(2)
    ll.pushBack(5)
    print("Trạng thái danh sách liên kết: ", end="")
    print_singly_list(ll.head)
