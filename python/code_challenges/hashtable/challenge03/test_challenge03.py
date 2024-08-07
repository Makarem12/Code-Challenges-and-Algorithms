# Write your test here
from challenge03 import *

def test_sum_of_unique_elements():
    assert sum_of_unique_elements([1, 2, 3, 2]) == 4
    assert sum_of_unique_elements([1, 2, 3, 4, 5]) == 15
    assert sum_of_unique_elements([1, 1, 1, 1]) == 0
    assert sum_of_unique_elements([]) == 0
    assert sum_of_unique_elements([1, 2, 2, 3, 3, 4, 4, 5, 5]) == 1
    assert sum_of_unique_elements([-1, -2, -3, -2]) == -4
    assert sum_of_unique_elements([1, 1, 2, 2, 3, 3, 4, 4, 5]) == 5
