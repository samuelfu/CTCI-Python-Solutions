class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_list(head: ListNode):
    while head:
        if head.next:
            print(head.val, end = " -> ")
        else:
            print(head.val)
        head = head.next

def create_list(linkedlist):
    head = ListNode(linkedlist[0])
    head_copy = head
    for item in linkedlist[1:]:
        node = ListNode(item)
        head.next = node
        head = head.next
    return head_copy
