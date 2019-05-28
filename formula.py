from math import sqrt, pi, pow, e, erf


def single_normal_distribution_value(x, std_dev, mean):
    return (1 / (std_dev * sqrt(2 * pi))) * (pow(e, (-(pow(x - mean, 2)) / (2 * std_dev * std_dev))))


def single_normal_distribution_integral_value(lower_bound, upper_bound, std_dev, mean):
    return -0.5 * (erf((mean - upper_bound) / (sqrt(2) * std_dev)) - (erf((mean - lower_bound) / (sqrt(2) * std_dev))))
