class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert_after_node(before_node, new_node):
    """
    Inserts a new node after the given node in a linked list.

    Parameters:
    before_node (ListNode): The node after which the new node will be inserted.
    new_node (ListNode): The new node to be inserted after the before_node.
    """
    new_node.next = before_node.next
    before_node.next = new_node
    
def linked_list_to_list(head):
    """
    Converts a linked list to a Python list for easy comparison in tests.

    Parameters:
    head (ListNode): The head node of the linked list.

    Returns:
    list: A list containing all values from the linked list.
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result