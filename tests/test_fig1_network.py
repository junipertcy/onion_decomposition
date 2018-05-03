# Adjacency matrix for the graph of Fig. 1 in Ref. 1, specifically:
#
#       9--8--10        11-----      15
#          |            |     |      |
# 0--1--2--3--4--5------6-----7------14
#                       |    / \     |
#                       ----12-13    16

import igraph as ig
import numpy as np

from onion_decomposition import od

g = ig.Graph()  # undirected graph object in igraph
g.add_vertices(17)

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 8)
g.add_edge(8, 9)
g.add_edge(8, 10)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 11)
g.add_edge(6, 7)
g.add_edge(6, 12)
g.add_edge(11, 7)
g.add_edge(7, 12)
g.add_edge(7, 13)
g.add_edge(12, 13)
g.add_edge(7, 14)
g.add_edge(14, 15)
g.add_edge(14, 16)

A = g.get_adjacency().data
m = np.array(A)


def test_fig1_network():
    corelist, layerlist = od.compute(m)
    criterion_1 = list(corelist) == [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1]
    criterion_2 = list(layerlist) == [1, 2, 3, 4, 5, 6, 8, 8, 2, 1, 1, 7, 8, 7, 2, 1, 1]
    if criterion_1 and criterion_2:
        _assert = True
    else:
        _assert = False

    assert _assert
