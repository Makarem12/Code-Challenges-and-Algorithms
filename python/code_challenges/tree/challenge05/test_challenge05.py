# Write your test here
from challenge05 import *
def test_maxHeight():
    tree = TreeNode(10)
    tree.left = TreeNode(20, TreeNode(40), TreeNode(28, None, TreeNode(29)))
    tree.right = TreeNode(30, TreeNode(27), TreeNode(50))

    assert maxHeight(tree) - 1 == 3