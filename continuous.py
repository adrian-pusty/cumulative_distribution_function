from math import inf

import pandas as pd

from formula import single_normal_distribution_integral_value, single_normal_distribution_value


def my_nd(xs, std_dev, mean):
    return [single_normal_distribution_value(x, std_dev, mean) for x in xs]


def my_cdf_erf(xs, std_dev, mean):
    return pd.DataFrame([single_normal_distribution_integral_value(-inf, x, std_dev, mean) for x in xs])


def my_cumsum(p):
    cumsum = list()
    current_value = 0.0
    for value in p:
        current_value += value
        cumsum.append(current_value)
    return pd.DataFrame(cumsum)



