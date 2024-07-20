# Write here the code challenge solution
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def maxHeight(root):
    if root is None:
        return 0
    else:
        left_height = maxHeight(root.left)
        right_height = maxHeight(root.right)
        return max(left_height, right_height) + 1




