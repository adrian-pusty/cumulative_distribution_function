from math import inf

import pandas as pd

from controller.formula import single_normal_distribution_integral_value, single_normal_distribution_value


def normal_distribution(xs, std_dev, mean):
    return pd.DataFrame([single_normal_distribution_value(x, std_dev, mean) for x in xs])


def cumulative_distribution_function(xs, std_dev, mean):
    """
        Wolfram Alpha example:
        integrate (1/(s*(sqrt(2*pi))))*e^(-((x-m)^2)/(2*s*s)) from -inf to 19
    """
    return pd.DataFrame([single_normal_distribution_integral_value(-inf, x, std_dev, mean) for x in xs])
