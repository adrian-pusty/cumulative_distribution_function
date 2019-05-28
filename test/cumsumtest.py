import numpy as np
from continuous import my_nd, my_cumsum


def test_cumsum():
    p = my_nd(np.array(range(-20, 21)), 2, 5)
    cumsum_diff = my_cumsum(p) - np.cumsum(p)
    assert np.sum(cumsum_diff[0].values) == 0.0
