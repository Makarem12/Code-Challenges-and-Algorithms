class ListNode:
    """
    Class representing a node in a singly linked list.

    Attributes:
        val (int): The value of the node.
        next (ListNode): A reference to the next node in the list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    """
    Reverses a singly linked list.

    Args:
        head (ListNode): The head node of the linked list.

    Returns:
        ListNode: The new head node of the reversed linked list.
    """
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

def printList(head):
    """
    Prints the values in the linked list from the head to the end.

    Args:
        head (ListNode): The head node of the linked list.
    """
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    # Example usage
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print("Original list:")
    printList(node1)

    reversed_head = reverseList(node1)

    print("Reversed list:")
    printList(reversed_head)
