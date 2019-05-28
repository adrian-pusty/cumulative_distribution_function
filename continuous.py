from math import inf

import pandas as pd

from formula import single_normal_distribution_integral_value, single_normal_distribution_value


def my_nd(xs, std_dev, mean):
    return pd.DataFrame([single_normal_distribution_value(x, std_dev, mean) for x in xs])


def my_cdf_erf(xs, std_dev, mean):
    """
        Wolfram Alpha example:
        integrate (1/(s*(sqrt(2*pi))))*e^(-((x-m)^2)/(2*s*s)) from -inf to 19
    """
    return pd.DataFrame([single_normal_distribution_integral_value(-inf, x, std_dev, mean) for x in xs])


def my_cumsum(p):
    cumsum = list()
    current_value = 0.0
    for value in p[0].values:
        current_value += value
        cumsum.append(current_value)
    return pd.DataFrame(cumsum)



