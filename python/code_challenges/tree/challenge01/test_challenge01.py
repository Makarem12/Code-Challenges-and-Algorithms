# Write your test here
# test_tree_builder.py
import pytest
from challenge01 import buildTree, printTree

def test_example1():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = buildTree(preorder, inorder)
    expected_output = [3, 9, 20, None, None, 15, 7]
    assert printTree(root) == expected_output

def test_example2():
    preorder = [-1]
    inorder = [-1]
    root = buildTree(preorder, inorder)
    expected_output = [-1]
    assert printTree(root) == expected_output


def test_single_node():
    preorder = [1]
    inorder = [1]
    root = buildTree(preorder, inorder)
    expected_output = [1]
    assert printTree(root) == expected_output
