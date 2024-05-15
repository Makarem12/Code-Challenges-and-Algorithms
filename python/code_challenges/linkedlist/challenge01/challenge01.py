# Write here the code challenge solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

