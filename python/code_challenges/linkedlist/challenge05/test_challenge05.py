# Write your test here
import pytest
from challenge05 import *

def test_insert_after_node():
    # Test case 1: Insert in the middle
    head = ListNode(1)
    node2 = ListNode(2)
    node4 = ListNode(4)
    node5 = ListNode(5)
    head.next = node2
    node2.next = node4
    node4.next = node5

    new_node = ListNode(3)
    insert_after_node(node2, new_node)

    assert linked_list_to_list(head) == [1, 2, 3, 4, 5]

    # Test case 2: Insert at the end
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    head.next = node2
    node2.next = node3

    new_node = ListNode(4)
    insert_after_node(node3, new_node)

    assert linked_list_to_list(head) == [1, 2, 3, 4]

    # Test case 3: Insert after the head
    head = ListNode(1)
    node3 = ListNode(3)
    node4 = ListNode(4)
    head.next = node3
    node3.next = node4

    new_node = ListNode(2)
    insert_after_node(head, new_node)

    assert linked_list_to_list(head) == [1, 2, 3, 4]

    # Test case 4: Insert into a single node list
    head = ListNode(1)

    new_node = ListNode(2)
    insert_after_node(head, new_node)

    assert linked_list_to_list(head) == [1, 2]

if __name__ == "__main__":
    pytest.main()
