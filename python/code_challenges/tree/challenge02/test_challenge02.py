from challenge02 import *

def test_trees():
    tree1 = Tree()
    tree1.root = Node(1)
    tree1.root.left = Node(2)
    tree1.root.right = Node(3)

    tree2 = Tree()
    tree2.root = Node(1)
    tree2.root.left = Node(2)
    tree2.root.right = Node(3)

    actual = pre_order(tree1.root)
    expected = pre_order(tree2.root)
    assert actual == expected
