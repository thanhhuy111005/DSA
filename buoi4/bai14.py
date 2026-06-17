def bai_14(head):
    """Cài đặt selection sort trên danh sách liên kết đơn[cite: 48, 49]."""
    curr = head
    while curr:
        min_node = curr
        search = curr.next
        while search:
            if search.data < min_node.data: min_node = search
            search = search.next
        curr.data, min_node.data = min_node.data, curr.data
        curr = curr.next
    return head

