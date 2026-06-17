def bai_40(head):
    """Cài đặt insertion sort trên danh sách liên kết đơn[cite: 147, 148]."""
    if not head or not head.next: return head
    sorted_list = None
    curr = head
    while curr:
        next_node = curr.next
        if not sorted_list or sorted_list.data >= curr.data:
            curr.next = sorted_list
            sorted_list = curr
        else:
            search = sorted_list
            while search.next and search.next.data < curr.data:
                search = search.next
            curr.next = search.next
            search.next = curr
        curr = next_node
    return sorted_list

class bai_41:
    """Mô phỏng sắp xếp trực tuyến (online): giữ mảng luôn sắp xếp sau mỗi phần tử mới[cite: 151, 152]."""
    def __init__(self):
        self.arr = []
    def add_element(self, x):
        self.arr.append(x)
        i = len(self.arr) - 2
        while i >= 0 and self.arr[i] > x:
            self.arr[i + 1] = self.arr[i]
            i -= 1
        self.arr[i + 1] = x
        return self.arr

