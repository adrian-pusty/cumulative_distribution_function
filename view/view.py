from matplotlib import pyplot as plt


def plot_functions(nd, cdf, xs, std_dev, mean):
    plt.subplot(2, 1, 1)
    plt.title('Normal Distribution and Cumulative Distribution Function\n '
              'Parameters: mean = ' + str(mean) + ', standard deviation = ' + str(std_dev))
    plt.plot(xs, nd, 'red', label='Normal Distribution')
    plt.ylabel('P(x)')

    plt.subplot(2, 1, 2)
    plt.plot(xs, cdf, 'blue', label='Cumulative Distribution Function')
    plt.ylabel('CDF(x)')
    plt.xlabel('x')

    plt.show()
