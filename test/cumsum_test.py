import pandas as pd
import numpy as np
from controller.formula_to_df import normal_distribution


def my_cumsum(p):
    cumsum = list()
    current_value = 0.0
    for value in p[0].values:
        current_value += value
        cumsum.append(current_value)
    return pd.DataFrame(cumsum)


def test_cumsum():
    p = normal_distribution(np.array(range(-20, 21)), 2, 5)
    cumsum_diff = my_cumsum(p) - np.cumsum(p)
    assert np.sum(cumsum_diff[0].values) == 0.0
