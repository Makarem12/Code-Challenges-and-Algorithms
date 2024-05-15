# Write your test here
from challenge01 import *
def test_delete_node():
    node1 = ListNode(4)
    node2 = ListNode(5)
    node3 = ListNode(1)
    node4 = ListNode(9)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    # Delete node with value 5
    deleteNode(node2)
    assert node1.val == 4
    assert node1.next.val == 1
    assert node1.next.next.val == 9
    assert node1.next.next.next == None

    node1 = ListNode(4)
    node2 = ListNode(5)
    node3 = ListNode(1)
    node4 = ListNode(9)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    # Delete node with value 1
    deleteNode(node3)
    assert node1.val == 4
    assert node1.next.val == 5
    assert node1.next.next.val == 9
    assert node1.next.next.next == None

# Run the test function
test_delete_node()
