import numpy as np
from app.series import normal_distribution, my_cumsum


def test_cumsum():
    p = normal_distribution(np.array(range(-20, 21)), 2, 5)
    cumsum_diff = my_cumsum(p) - np.cumsum(p)
    assert np.sum(cumsum_diff[0].values) == 0.0
