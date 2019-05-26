from ListNode import ListNode, print_list, create_list

def remove_dups(head: ListNode) -> ListNode:
    """
    Write code to remove duplicates from an unsorted linked list.
    How would you solve this problem if a temporary buffer is not allowed?
    """

    p1 = head

    while p1:
        p2 = p1
        while p2.next:
            if p2.next.val == p1.val:
                p2.next = p2.next.next
            else:
                p2 = p2.next
        p1 = p1.next

    return head

print_list(remove_dups(create_list((3,3,6,4,4,5,6))))
