# Write here the code challenge solution
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        Check if the stack is empty.
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Push an item onto the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Pop an item from the stack.
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def size(self):
        """
        Get the size of the stack.
        """
        return len(self.items)

    def __str__(self):
        return str(self.items)


def delete_middle(stack):
    def delete_middle_helper(stack, current_index, size):
        # Base case: if the current index is equal to size // 2, we pop the middle element
        if current_index == size // 2:
            stack.pop()
            return
        
        # Pop the top element and hold it temporarily
        top_element = stack.pop()
        
        # Recursive call to reach the middle element
        delete_middle_helper(stack, current_index + 1, size)
        
        # Push the top element back after removing the middle element
        stack.push(top_element)
    
    # Get the size of the stack
    size = stack.size()
    
    # Start the recursive helper function
    delete_middle_helper(stack, 0, size)
    return stack


# Example usage
stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)
print("Original Stack:", stack1)
new_stack1 = delete_middle(stack1)
print("Stack after deleting middle element:", new_stack1)

stack2 = Stack()
stack2.push(1)
stack2.push(2)
stack2.push(3)
stack2.push(4)
print("Original Stack:", stack2)
new_stack2 = delete_middle(stack2)
print("Stack after deleting middle element:", new_stack2)
