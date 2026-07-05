def cau_36():
    print("\n--- Câu 36. Đảo ngược danh sách ---")

    class Node:

        def __init__(self, val=0):
            self.val = val
            self.next = None

    # Tạo danh sách mẫu: 1 -> 2 -> 3 -> null
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    # Giải thuật lặp 3 con trỏ tại chỗ
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # In thử chuỗi kết quả
    nodes = []
    while prev:
        nodes.append(str(prev.val))
        prev = prev.next
    nodes.append("null")
    print(f"Chuỗi sau khi đảo lặp: {' -> '.join(nodes)}")
