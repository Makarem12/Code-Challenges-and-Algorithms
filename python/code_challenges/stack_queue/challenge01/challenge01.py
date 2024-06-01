# Write here the code challenge solution
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.top is None:
            raise IndexError("pop from empty stack")
        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return value

    def peek(self):
        if self.top is None:
            raise IndexError("peek from empty stack")
        return self.top.value

    def is_empty(self):
        return self.top is None

    def get_size(self):
        return self.size
class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x):
        self.stack1.push(x)

    def pop(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

    def empty(self) -> bool:
        return self.stack1.is_empty() and self.stack2.is_empty()

    def size(self) -> int:
        return self.stack1.get_size() + self.stack2.get_size()

# Example usage
if __name__ == "__main__":
    myQueue = MyQueue()
    myQueue.push(1)   # queue is: [1]
    myQueue.push(2)   # queue is: [1, 2] (leftmost is front of the queue)
    print(myQueue.peek())  # returns 1
    print(myQueue.pop())   # returns 1, queue is [2]
    print(myQueue.empty()) # returns False
    print(myQueue.size())  # returns 1, as there's one element left in the queue

    

