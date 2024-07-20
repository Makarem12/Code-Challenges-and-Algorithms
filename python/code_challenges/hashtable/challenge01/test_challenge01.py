# Write your test here
from challenge01 import *


def test_findTarget():
    tree = TreeNode(7)
    tree.left = TreeNode(2, TreeNode(1), TreeNode(5))
    tree.right = TreeNode(9, None, TreeNode(14))

    assert findTarget(tree, 3) == True
    assert findTarget(tree, 4) == False
    assert findTarget(tree, 6) == True 
    assert findTarget(tree, 20) == False




