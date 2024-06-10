from queue import Queue

def reverse_queue(queue):
    stack = []
    
    # Dequeue all elements from the queue and push them onto the stack
    while not queue.empty():
        stack.append(queue.get())
    
    # Pop all elements from the stack and enqueue them back into the queue
    while stack:
        queue.put(stack.pop())
    
    return queue
