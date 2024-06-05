from challenge03 import *
def test_delete_middle():
    stack1 = Stack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.push(4)
    stack1.push(5)
    stack1 = delete_middle(stack1)
    assert stack1.items == [1, 2, 4, 5]

    stack2 = Stack()
    stack2.push(1)
    stack2.push(2)
    stack2.push(3)
    stack2.push(4)
    stack2 = delete_middle(stack2)
    assert stack2.items == [1, 3, 4]

    stack3 = Stack()
    stack3.push(10)
    stack3.push(20)
    stack3.push(30)
    stack3.push(40)
    stack3.push(50)
    stack3.push(60)
    stack3.push(70)
    stack3 = delete_middle(stack3)
    assert stack3.items == [10, 20, 30, 50, 60, 70]

    stack4 = Stack()
    stack4.push(1)
    stack4 = delete_middle(stack4)
    assert stack4.items == []

    stack5 = Stack()
    stack5.push(1)
    stack5.push(2)
    stack5 = delete_middle(stack5)
    assert stack5.items == [2]
