def cau_40():
    print("\n--- Câu 40. Sắp xếp linked list ---")

    class Node:

        def __init__(self, val=0):
            self.val = val
            self.next = None

    head = Node(3)
    head.next = Node(1)
    head.next.next = Node(2)

    def merge_sort_list(h):
        if not h or not h.next:
            return h
        
        # Tách đôi danh sách bằng kỹ thuật slow/fast
        slow, fast = h, h.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None  # Cắt xẻ chuỗi làm 2 độc lập

        # Trộn đệ quy
        left = merge_sort_list(h)
        right = merge_sort_list(mid)

        # Merge hai chuỗi đã xếp
        dummy = Node(0)
        tail = dummy
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left if left else right
        return dummy.next

    sorted_head = merge_sort_list(head)
    res = []
    while sorted_head:
        res.append(str(sorted_head.val))
        sorted_head = sorted_head.next
    print(f"Chuỗi sau khi sắp xếp chuẩn bằng Merge Sort: {' -> '.join(res)}")
