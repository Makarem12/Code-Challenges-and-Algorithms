# Write your test here
# test_linked_list.py
import pytest
from challenge04 import *

def create_linked_list(nums):
    """
    Helper function to create a linked list from a list of numbers.
    """
    if not nums:
        return None
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

def linked_list_to_list(head):
    """
    Helper function to convert a linked list to a list of its values.
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_reverseList():
    # Test empty list
    assert reverseList(None) is None

    # Test list with one element
    head = create_linked_list([1])
    assert linked_list_to_list(reverseList(head)) == [1]

    # Test list with multiple elements
    head = create_linked_list([1, 2, 3, 4, 5])
    assert linked_list_to_list(reverseList(head)) == [5, 4, 3, 2, 1]

def test_printList(capsys):
    # Test empty list
    printList(None)
    captured = capsys.readouterr()
    assert captured.out.strip() == "None"

    # Test list with one element
    head = create_linked_list([1])
    printList(head)
    captured = capsys.readouterr()
    assert captured.out.strip() == "1 -> None"

    # Test list with multiple elements
    head = create_linked_list([1, 2, 3, 4, 5])
    printList(head)
    captured = capsys.readouterr()
    assert captured.out.strip() == "1 -> 2 -> 3 -> 4 -> 5 -> None"

if __name__ == "__main__":
    pytest.main([__file__])

