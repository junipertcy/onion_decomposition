import numpy as np


def compute(mat):
    """
    Compute the onion decomposition.

    Parameters
    ----------
    mat: `numpy.ndarray`
        The adjacency matrix of the network.

    Returns
    -------
    corelist: `numpy.ndarray`
        The coreness of each node.
    layerlist: `numpy.ndarray`
        The layerness of each node.

    """
    m, n = mat.shape
    assert m == n, "Adjacency matrix must be square"
    assert np.array_equal(mat, mat.transpose()), "Adjaceny matrix must be symmetric"
    deg = np.resize(np.sum(mat, 0), m).astype(int)
    core = layer = 1

    unexplored_vtx = np.full(m, True)

    corelist = np.zeros(m)
    layerlist = np.zeros(m)

    while np.any(unexplored_vtx):
        this_layer = np.full(m, False)
        this_layer = [True if (deg_ <= core and unexplored_vtx[idx]) else False for idx, deg_ in enumerate(deg)]
        for vtx_idx, vtx in enumerate(this_layer):
            if vtx:
                corelist[vtx_idx] = core
                layerlist[vtx_idx] = layer
                for target_vtx_idx, target_vtx in enumerate(mat[vtx_idx]):
                    if target_vtx == 1:
                        deg[target_vtx_idx] -= 1
                unexplored_vtx[vtx_idx] = False
        layer += 1
        deg_for_core = [deg[idx] for idx, d in enumerate(unexplored_vtx) if d]
        if len(deg_for_core) > 0 and min(deg_for_core) >= core + 1:
            core = min(deg_for_core)

    return corelist.astype(int), layerlist.astype(int)


def onion_spectrum(coreness, layerness):
    """
    Compute the onion spectrum.

    Parameters
    ----------
    coreness: `numpy.ndarray`
        The coreness of each node.
    layerness: `numpy.ndarray`
        The layerness of each node.

    Returns
    -------
    lines: `list`
        A list of `list` objects that contain fraction of nodes within each layer.
        The length of `lines` indicates the maximum coreness of the network.
    x_ranges: `list`
        A list of `range` objects that act as ticks for the x-axes.

    """
    n_layer = {}
    for layer in layerness:
        n_layer[layer] = [0, 0]
    for idx, core in enumerate(coreness):
        n_layer[layerness[idx]][0] += 1 / len(coreness)
        n_layer[layerness[idx]][1] = core
    lines = []
    x_ranges = []
    line = []
    x_range = []
    
    layer_ = 1
    for layer in range(1, max(layerness) + 1):
        if n_layer[layer][1] == layer_:
            line += [n_layer[layer][0]]
            x_range += [layer]
        elif n_layer[layer][1] == layer_ + 1:
            lines += [line]
            x_ranges += [x_range]
            line = [n_layer[layer][0]]
            x_range = [layer]
            layer_ += 1
    lines += [line] 
    x_ranges += [x_range]
    return lines, x_ranges
