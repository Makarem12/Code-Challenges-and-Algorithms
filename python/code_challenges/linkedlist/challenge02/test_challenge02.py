# Write your test here
from challenge02 import *

def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

#the first test
def test_middle_node():
    input_list = [1, 2, 3, 4, 5]
    head = list_to_linked_list(input_list)
    middle = middleNode(head)
    actual = linked_list_to_list(middle)
    expected = [3, 4, 5]
    assert actual == expected, f"Expected {expected}, but got {actual}"

#the second test
def test_middle_node_even():
    input_list = [1, 2, 3, 4, 5, 6]
    head = list_to_linked_list(input_list)
    middle = middleNode(head)
    actual = linked_list_to_list(middle)
    expected = [4, 5, 6]
    assert actual == expected, f"Expected {expected}, but got {actual}"    
