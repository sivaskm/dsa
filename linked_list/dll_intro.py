# Node
class Node:
    def __init__(self, data, next=None, back=None):
        self.data = data
        self.next: Node = next
        self.back: Node = back


def print_ll(head: Node):
    while head:
        print(head.data, end=" -> ")
        head = head.next


def create_ll_from_arr(arr):
    head = Node(arr[0])
    prev = head
    for element in arr[1:]:
        temp = Node(data=element, back=prev)
        prev.next = temp
        prev = temp
    return head


def delete_head(head: Node | None):
    if head is None or head.next is None:
        return None
    prev = head
    head = head.next
    head.prev = None
    prev.next = None
    return head


def delete_tail(head: Node | None):
    if head is None or head.next is None:
        return None
    mover = head

    # while mover.next.next:
    #     mover = mover.next
    # mover.next.back = None
    # mover.next = None
    # return head

    # another method
    while mover.next:
        mover = mover.next
    prev = mover.back
    prev.next = None
    mover.back = None
    return head


def delete_at_position(head: Node | None, position: int):
    if head is None or head.next is None:
        return None
    if position == 1:
        return delete_head(head=head)
    mover = head
    count = 0
    while mover:
        count += 1
        if count == position - 1:
            mover.next = mover.next.next
            mover.next.back = mover
        mover = mover.next
    return head


arr = [1, 3, 5, 6, 7, 10, 20]
ll = create_ll_from_arr(arr)
# print_ll(ll)
# print_ll(delete_head(ll))
print_ll(delete_tail(ll))
# print_ll(delete_at_position(ll, 51))
