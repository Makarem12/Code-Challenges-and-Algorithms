
from challenge05 import intersection  # Replace with the actual module name

def test_intersection():
    assert intersection([1, 2, 2, 1], [2, 2]) == [2]
    assert intersection([1, 2, 3, 4], [4, 3, 2, 1]) == [4,3,2,1]
    assert intersection([4, 9, 5], [9, 4, 9, 8, 4]) == [9,4]
    assert intersection([], [1, 2, 3]) == []
    assert intersection([1, 2, 3], []) == []
    assert intersection([1, 1, 1, 1], [1, 1, 1, 1]) == [1]
    assert intersection([1, 2, 3], [4, 5, 6]) == []

