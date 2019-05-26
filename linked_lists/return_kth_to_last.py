from ListNode import ListNode, print_list, create_list

def return_kth_to_last(head: ListNode, k: int) -> int:
    """
    Implement an algorithm to find the kth to last element of a singly linked list
    """

    p1 = head
    p2 = head
    for x in range(k):
        p2 = p2.next
    while p2:
        p1 = p1.next
        p2 = p2.next
    return p1.val

print(return_kth_to_last(create_list((3, 4, 5, 6, 7)), 3))
