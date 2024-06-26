class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

# Initialize tree1
tree1 = Tree()
tree1.root = Node(1)
tree1.root.left = Node(2)
tree1.root.right = Node(3)

# Initialize tree2
tree2 = Tree()
tree2.root = Node(1)
tree2.root.left = Node(2)
tree2.root.right = Node(3)

def pre_order(root):
    result = []
    def traverse(node):
        if node:
            result.append(node.value)
            traverse(node.left)
            traverse(node.right)
    traverse(root)
    return result
