import numpy as np
import json

from app.plotutil import plot_data
from app.series import my_cdf_erf, normal_distribution

data = None
with open("app/parameters.json", "r") as f:
    data = json.load(f)

xs = np.array(range(data['rangeStart'], data['rangeStop']))

p = normal_distribution(xs, data['standardDeviation'], data['mean'])
cdf_erf = my_cdf_erf(xs, data['standardDeviation'], data['mean'])

print(cdf_erf[0].values[-1])
plot_data(xs, p, cdf_erf)


