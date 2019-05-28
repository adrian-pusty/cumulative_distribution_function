import numpy as np
from matplotlib import pyplot as plt

from continuous import my_cdf_erf, my_nd

xs = np.array(range(-100, 101))
std_dev = 20
mean = 3

p = my_nd(xs, std_dev, mean)
cdf_erf = my_cdf_erf(xs, std_dev, mean)

print(cdf_erf[0].values[-1])
plt.plot(xs, cdf_erf)
plt.show()
plt.plot(xs, p)
plt.show()


