from matplotlib import pyplot as plt


def plot_functions(xs, nd, cdf):
    plt.subplot(2, 1, 1)
    plt.title('Normal Distribution and Cumulative Distribution Function')
    plt.plot(xs, nd, 'red', label='Normal Distribution')
    plt.ylabel('P(x)')

    plt.subplot(2, 1, 2)
    plt.plot(xs, cdf, 'blue', label='Cumulative Distribution Function')
    plt.ylabel('CDF(x)')
    plt.xlabel('x')

    plt.show()
