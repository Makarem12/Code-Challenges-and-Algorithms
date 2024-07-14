from collections import deque

class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        """
        Initializes a TreeNode with the given value and optional left and right children.
        """
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    """
    Constructs a height-balanced binary search tree (BST) from a sorted integer array.
    """
    def convertListToBST(left, right):
        """
        Recursively constructs a BST from the given range of indices in the sorted array.
        """
        if left > right:
            return None
        
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        
        node.left = convertListToBST(left, mid - 1)
        node.right = convertListToBST(mid + 1, right)
        
        return node

    return convertListToBST(0, len(nums) - 1)

def printLevelOrder(root):
    """
    Performs level-order traversal of a binary tree and returns the node values in a list.
    """
    if not root:
        return []
    
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
    
    # Trim trailing None values from the end
    while result and result[-1] is None:
        result.pop()
    
    return result
