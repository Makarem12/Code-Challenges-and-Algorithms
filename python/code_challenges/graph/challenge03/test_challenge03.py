
from challenge03 import Graph  # Replace 'your_module' with the actual module name where your Graph class is located.

def test_graph_strongly_connected():
    # Test Case 1: Not Strongly Connected Graph
    numbers1 = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 4], [1, 7], [7, 3]]
    g1 = Graph(8)
    for u, v in numbers1:
        g1.add_edge(u, v)
    assert g1.is_strongly_connected() == "Not strongly connected"

    # Test Case 2: Strongly Connected Graph
    numbers2 = [[1, 2], [1, 0], [0, 4], [4, 3], [3, 2], [3, 1], [2, 1], [2, 4]]
    g2 = Graph(5)
    for u, v in numbers2:
        g2.add_edge(u, v)
    assert g2.is_strongly_connected() == "Strongly connected"

    # Test Case 3: Single Node Graph (trivially strongly connected)
    g3 = Graph(1)
    assert g3.is_strongly_connected() == "Strongly connected"

    # Test Case 4: Disconnected Graph
    numbers4 = [[0, 1], [2, 3]]
    g4 = Graph(4)
    for u, v in numbers4:
        g4.add_edge(u, v)
    assert g4.is_strongly_connected() == "Not strongly connected"

    # Test Case 5: Circular Strongly Connected Graph
    numbers5 = [[0, 1], [1, 2], [2, 0]]
    g5 = Graph(3)
    for u, v in numbers5:
        g5.add_edge(u, v)
    assert g5.is_strongly_connected() == "Strongly connected"



