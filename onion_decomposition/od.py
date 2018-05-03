import numpy as np


def compute(mat):
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

