import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from continuous import my_cumsum, my_cdf_erf, my_nd

xs = np.array(range(-20, 21))
std_dev = 2
mean = 5
p = my_nd(xs, std_dev, mean)


cumsum = np.cumsum(p)
cumsum_mine = my_cumsum(p)
cdf_erf = my_cdf_erf(xs, std_dev, mean)

p = pd.DataFrame(p)
# dystrybuanta_python = np.cumsum(p)

# print(p)
# plt.plot(x, p)
print(np.sum(p))
print(cdf_erf)
plt.plot(xs, cdf_erf)
plt.show()


# (1/(2*(sqrt(2*pi))))*e^(-((x-5)^2)/(2*2*2))
# integrate (1/(s*(sqrt(2*pi))))*e^(-((x-m)^2)/(2*s*s)) from 0 to 1
# integrate (1/(2*(sqrt(2*pi))))*e^(-((x-5)^2)/(2*2*2)) from -inf to -19