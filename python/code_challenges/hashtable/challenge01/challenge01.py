class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def findTarget(root, k):
    if not root:
        return False

    def inorder_traversal(node, elements):
        if not node:
            return False
        if inorder_traversal(node.left, elements):
            return True
        if k - node.value in elements:
            return True
        elements.add(node.value)
        return inorder_traversal(node.right, elements)

    return inorder_traversal(root, set())


