def bai_26():
    print("\n--- Bài 26 (Bài 11 LL): Danh sách liên kết đôi ---")

    class DoublyNode:

        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    class DoublyLinkedList:

        def __init__(self):
            self.head = None
            self.tail = None

        def pushFront(self, data):
            new_node = DoublyNode(data)
            if not self.head:
                self.head = self.tail = new_node
                return
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        def pushBack(self, data):
            new_node = DoublyNode(data)
            if not self.tail:
                self.head = self.tail = new_node
                return
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        def display_forward(self):
            curr = self.head
            res = []
            while curr:
                res.append(str(curr.data))
                curr = curr.next
            print("Duyệt xuôi: " + " <-> ".join(res))

    dll = DoublyLinkedList()
    dll.pushFront(10)
    dll.pushBack(20)
    dll.display_forward()
