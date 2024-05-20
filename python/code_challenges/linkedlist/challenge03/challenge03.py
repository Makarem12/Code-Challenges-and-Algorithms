class ListNode:
    def __init__(self, val=0, next=None):
        """
        Initialize a new ListNode.

        Args:
        val (int): The value of the node.
        next (ListNode, optional): The next node in the list. Defaults to None.
        """
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    """
    Remove the nth node from the end of the linked list and return its head.

    Args:
    head (ListNode): The head of the linked list.
    n (int): The position from the end of the list of the node to remove.

    Returns:
    ListNode: The head of the modified linked list.
    """
    dummy = ListNode(0, head)
    fast = slow = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next

def list_to_linked_list(lst):
    """
    Convert a list to a linked list.

    Args:
    lst (list): The list to convert.

    Returns:
    ListNode: The head of the linked list.
    """
    head = ListNode(lst[0]) if lst else None
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_list(head):
    """
    Convert a linked list to a list.

    Args:
    head (ListNode): The head of the linked list.

    Returns:
    list: The list representation of the linked list.
    """
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst
