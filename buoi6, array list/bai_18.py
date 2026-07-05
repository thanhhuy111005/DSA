def bai_18():
    print("\n--- Bài 18 (Bài 3 LL): Tìm kiếm một giá trị ---")

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    def search_value(target):
        curr = head
        idx = 0
        while curr:
            if curr.data == target:
                return idx
            curr = curr.next
            idx += 1
        return -1

    def print_singly_list(head):
        curr = head
        nodes = []
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next
        nodes.append("null")
        print(" -> ".join(nodes))

    print("Danh sách: ", end="")
    print_singly_list(head)
    print(f"Tìm giá trị 2 -> Vị trí chỉ số: {search_value(2)}")
    print(f"Tìm giá trị 9 -> Vị trí chỉ số: {search_value(9)}")
