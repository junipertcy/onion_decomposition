#      1-----
#     / \   |
# 4--0---3  |
#     \ /   |
#      2-----


import igraph as ig
import numpy as np

from onion_decomposition import od

g = ig.Graph()  # undirected graph object in igraph
g.add_vertices(5)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

A = g.get_adjacency().data
m = np.array(A)


def test_no_core2_network():
    corelist, layerlist = od.compute(m)
    criterion_1 = list(corelist) == [3, 3, 3, 3, 1]
    criterion_2 = list(layerlist) == [2, 2, 2, 2, 1]
    if criterion_1 and criterion_2:
        _assert = True
    else:
        _assert = False

    assert _assert
