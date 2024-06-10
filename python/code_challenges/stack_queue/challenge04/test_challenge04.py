from queue import Queue
import pytest
from challenge04 import reverse_queue  # Import the function from the function code file

# Helper function to convert queue to list for easy comparison
def queue_to_list(queue):
    lst = []
    while not queue.empty():
        lst.append(queue.get())
    return lst

def test_reverse_queue():
    # Test Case 1
    q1 = Queue()
    for i in [5, 4, 3, 2, 1]:
        q1.put(i)
    q1 = reverse_queue(q1)
    assert queue_to_list(q1) == [1, 2, 3, 4, 5]

    # Test Case 2
    q2 = Queue()
    for i in [10, 20, 30, 40, 50]:
        q2.put(i)
    q2 = reverse_queue(q2)
    assert queue_to_list(q2) == [50, 40, 30, 20, 10]

    # Test Case 3
    q3 = Queue()
    for i in [1, 2, 3]:
        q3.put(i)
    q3 = reverse_queue(q3)
    assert queue_to_list(q3) == [3, 2, 1]

    # Test Case 4: Edge case with empty queue
    q4 = Queue()
    q4 = reverse_queue(q4)
    assert queue_to_list(q4) == []

    # Test Case 5: Edge case with single element
    q5 = Queue()
    q5.put(42)
    q5 = reverse_queue(q5)
    assert queue_to_list(q5) == [42]

if __name__ == "__main__":
    pytest.main([__file__])
