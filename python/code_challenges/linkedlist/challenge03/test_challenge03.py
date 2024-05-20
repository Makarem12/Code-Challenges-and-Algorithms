from challenge03 import *

def test_remove_nth_from_end():
    """
    Test the removeNthFromEnd function with multiple test cases.
    """
    # Test case 1
    head1 = list_to_linked_list([1, 2, 3, 4, 5])
    n1 = 2
    new_head1 = removeNthFromEnd(head1, n1)
    assert linked_list_to_list(new_head1) == [1, 2, 3, 5]

    # Test case 2
    head2 = list_to_linked_list([1])
    n2 = 1
    new_head2 = removeNthFromEnd(head2, n2)
    assert linked_list_to_list(new_head2) == []

    # Test case 3
    head3 = list_to_linked_list([1, 2])
    n3 = 1
    new_head3 = removeNthFromEnd(head3, n3)
    assert linked_list_to_list(new_head3) == [1]

    # Additional test case
    head4 = list_to_linked_list([1, 2, 3])
    n4 = 3
    new_head4 = removeNthFromEnd(head4, n4)
    assert linked_list_to_list(new_head4) == [2, 3]

if __name__ == "__main__":
    import pytest

    # Running the tests
    pytest.main()

    # Printing results for demonstration
    def print_result(lst, n):
        """
        Helper function to demonstrate the result of removing the nth node from the end.

        Args:
        lst (list): The input list.
        n (int): The position from the end of the list of the node to remove.
        """
        head = list_to_linked_list(lst)
        new_head = removeNthFromEnd(head, n)
        print(f"Original list: {lst}")
        print(f"After removing {n}th from end: {linked_list_to_list(new_head)}\n")

    print_result([1, 2, 3, 4, 5], 2)
    print_result([1], 1)
    print_result([1, 2], 1)
    print_result([1, 2, 3], 3)
