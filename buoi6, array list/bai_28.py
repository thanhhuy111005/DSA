def bai_28():
    print("\n--- Bài 28 (Bài 13 LL): Sắp xếp danh sách liên kết ---")

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

    head = Node(3)
    head.next = Node(1)
    head.next.next = Node(2)
    print("Danh sách chưa sắp xếp: ", end="")
    print_singly_list(head)

    def get_mid(node):
        slow, fast = node, node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(l1, l2):
        dummy = Node(0)
        tail = dummy
        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2
        return dummy.next

    def merge_sort(h):
        if not h or not h.next:
            return h
        mid = get_mid(h)
        left = h
        right = mid.next
        mid.next = None

        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)
        return merge(sorted_left, sorted_right)

    head = merge_sort(head)
    print("Danh sách sau khi áp dụng Merge Sort: ", end="")
    print_singly_list(head)
