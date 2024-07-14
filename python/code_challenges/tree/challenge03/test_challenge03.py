import pytest
from challenge03 import sortedArrayToBST, printLevelOrder

def test_sortedArrayToBST():
    test_cases = [
        ([0, -3, -10, 5, 9], [-10, 0, 5, None, -3, None, 9]),  # Example 1
        ([3, 1], [3, None, 1]),  # Example 2
        ([], []),  # Empty input
        ([1], [1]),  # Single node
    ]
    
    for nums, expected_level_order in test_cases:
        root = sortedArrayToBST(nums)
        result_level_order = printLevelOrder(root)
        assert result_level_order == expected_level_order, f"For input {nums}, expected {expected_level_order}, but got {result_level_order}"

if __name__ == "__main__":
    pytest.main()
