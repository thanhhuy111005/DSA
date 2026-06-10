class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    p = head

    while p is not None:
        print(p.data, end=" -> ")
        p = p.next

    print("null")


def bubble_sort(head):
    if head is None:
        return head

    swapped = True

    while swapped:
        swapped = False
        p = head

        while p.next is not None:
            if p.data > p.next.data:
                p.data, p.next.data = p.next.data, p.data
                swapped = True

            p = p.next

    return head


head = Node(1)
head.next = Node(3)
head.next.next = Node(2)

print("Danh sách ban đầu:")
print_list(head)

bubble_sort(head)

print("Danh sách sau sắp xếp:")
print_list(head)