from challenge04 import *

def test_reorder_people_by_height():
    names = ["Alice", "Bob", "Bob"]
    heights = [155, 185, 150]
    expected_output = ["Bob", "Alice", "Bob"]
    assert reorder_people_by_height(names, heights) == expected_output

    names = ["John", "Jane", "Doe"]
    heights = [180, 170, 160]
    expected_output = ["John", "Jane", "Doe"]
    assert reorder_people_by_height(names, heights) == expected_output

   


