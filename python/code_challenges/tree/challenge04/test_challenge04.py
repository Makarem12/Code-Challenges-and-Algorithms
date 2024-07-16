# Write your test here
import pytest
from challenge04 import TreeNode, findMaxValue

def test_findMaxValue():
    # Test case 1: Normal tree
    root1 = TreeNode(1000)
    root1.left = TreeNode(500)
    root1.right = TreeNode(2000)
    root1.left.left = TreeNode(250)
    root1.left.right = TreeNode(600)
    root1.right.right = TreeNode(12000)
    assert findMaxValue(root1) == 12000

    # Test case 2: Single node
    root2 = TreeNode(1)
    assert findMaxValue(root2) == 1

    # Test case 3: Empty tree
    root3 = None
    assert findMaxValue(root3) == float('-inf')

    # Test case 4: Tree with all negative values
    root4 = TreeNode(-10)
    root4.left = TreeNode(-20)
    root4.right = TreeNode(-5)
    assert findMaxValue(root4) == -5

    # Test case 5: Tree with duplicates
    root5 = TreeNode(5)
    root5.left = TreeNode(5)
    root5.right = TreeNode(5)
    assert findMaxValue(root5) == 5

if __name__ == "__main__":
    pytest.main()
