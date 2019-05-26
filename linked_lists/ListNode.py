class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printList(head: ListNode):
    while head:
        print(head.val)
        head = head.next
