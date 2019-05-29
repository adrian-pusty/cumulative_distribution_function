from matplotlib import pyplot as plt


def plot_data(xs, p, cdf):
    plt.subplot(2, 1, 1)
    plt.title('Normal Distribution and Cumulative Distribution Function')
    plt.plot(xs, p, 'red', label='Normal Distribution')
    plt.ylabel('P(x)')

    plt.subplot(2, 1, 2)
    plt.plot(xs, cdf, 'blue', label='Cumulative Distribution Function')
    plt.ylabel('CDF(x)')
    plt.xlabel('x')

    plt.show()
