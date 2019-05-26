class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printList(head: ListNode):
    while head:
        print(head.val, end = " -> ")
        head = head.next
    print("None")

def createList(linkedlist):
    head = ListNode(linkedlist[0])
    head_copy = head
    for item in linkedlist[1:]:
        node = ListNode(item)
        head.next = node
        head = head.next
    return head_copy
