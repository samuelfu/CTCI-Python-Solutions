from ListNode import ListNode, print_list, create_list

def delete_middle_node(node: ListNode):
    """
    Implement an algorithm to delete a node in the middle of
    a singly linked list, given only access to that node
    """
    
    node.val = node.next.val
    node.next = node.next.next

ll = create_list((1,2,3,4,5))
ll = ll.next
delete_middle_node(ll)
