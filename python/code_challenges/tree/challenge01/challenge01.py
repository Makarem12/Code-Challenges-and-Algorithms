# tree_builder.py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    # The first element of preorder is the root value (root_val), which is then removed from the list.
    root_val = preorder.pop(0)
    root = TreeNode(root_val)

    inorder_index = inorder.index(root_val)

    root.left = buildTree(preorder, inorder[:inorder_index])
    root.right = buildTree(preorder, inorder[inorder_index + 1:])

    return root

# Helper function to print tree in level order for testing purposes
from collections import deque

def printTree(root):
    if not root:
        return "[]"
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    while result and result[-1] is None:
        result.pop()
    
    return result
