# Write your test here
import pytest
from challenge01 import * # Import the MyQueue class from the file where it's implemented

@pytest.fixture
def queue():
    return MyQueue()

def test_push(queue):
    queue.push(1)
    queue.push(2)
    assert queue.peek() == 1

def test_pop(queue):
    queue.push(1)
    queue.push(2)
    assert queue.pop() == 1
    assert queue.pop() == 2
    assert queue.empty() == True

def test_peek(queue):
    queue.push(1)
    queue.push(2)
    assert queue.peek() == 1
    queue.pop()
    assert queue.peek() == 2

def test_empty(queue):
    assert queue.empty() == True
    queue.push(1)
    assert queue.empty() == False
    queue.pop()
    assert queue.empty() == True

if __name__ == "__main__":
    pytest.main()
