
from challenge01 import Graph, Node

def test_bfs_traversal():
    graph1 = Graph()

    a = graph1.add_node('A')
    b = graph1.add_node('B')
    c = graph1.add_node('C')
    d = graph1.add_node('D')
    e = graph1.add_node('E')
    f = graph1.add_node('F')
    g = graph1.add_node('G')
    h = graph1.add_node('H')
    i = graph1.add_node('I')
    k = graph1.add_node('K')

    graph1.add_edge(a, c)
    graph1.add_edge(a, b)
    graph1.add_edge(c, e)
    graph1.add_edge(c, f)
    graph1.add_edge(b, d)
    graph1.add_edge(e, g)
    graph1.add_edge(d, i)
    graph1.add_edge(i, h)
    graph1.add_edge(h, k)

    assert graph1.bfs_traversal('A') == ['A', 'C', 'B', 'E', 'F', 'D', 'G', 'I', 'H', 'K']

    # Test BFS starting from another node
    assert graph1.bfs_traversal('C') == ['C', 'A', 'E', 'F', 'B', 'G', 'D', 'I', 'H', 'K']

    # Test BFS with a node that does not exist
    assert graph1.bfs_traversal('Z') == "Start node not found in the graph"

def test_add_node():
    graph1 = Graph()
    a = graph1.add_node('A')
    assert a.value == 'A'
    assert str(a) == 'A'

def test_add_edge():
    graph1 = Graph()
    a = graph1.add_node('A')
    b = graph1.add_node('B')
    c = graph1.add_node('C')

    graph1.add_edge(a, b)
    assert graph1.adj_list[a][0].vertex == b
    assert graph1.adj_list[b][0].vertex == a

    graph1.add_edge(a, c, 10)
    assert graph1.adj_list[a][1].vertex == c
    assert graph1.adj_list[a][1].weight == 10

    # Test adding an edge where one node does not exist
    d = Node('D')
    assert graph1.add_edge(d, b) == "A node does not exist"


