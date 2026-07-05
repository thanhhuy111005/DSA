def cau_39():
    print("\n--- Câu 39. Xóa nút thứ k từ cuối ---")

    class Node:

        def __init__(self, val=0):
            self.val = val
            self.next = None

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    k = 2

    dummy = Node(0)
    dummy.next = head
    fast = slow = dummy

    # Cho con trỏ fast đi trước k bước
    for _ in range(k):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next  # Ngắt liên kết cô lập nút thứ k cần gỡ

    # In kết quả chuỗi còn lại
    res = []
    curr = dummy.next
    while curr:
        res.append(str(curr.val))
        curr = curr.next
    res.append("null")
    print(f"Chuỗi sau khi xóa nút thứ {k} từ cuối: {' -> '.join(res)}")
