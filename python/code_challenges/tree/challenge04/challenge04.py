# Write here the code challenge solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    # Initialize an empty list to store the values
    values = []
    
    def traverse(node):
        if node:
            traverse(node.left)
            values.append(node.val)
            traverse(node.right)
    
    traverse(root)
    return values

def findMaxValue(root):
    if not root:
        return float('-inf')
    
    values = inorderTraversal(root)
    return max(values)

