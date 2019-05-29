from model.model import read_parameters
from controller.formulatodf import cumulative_distribution_function, normal_distribution
from view.view import plot_functions

xs, standard_deviation, mean = read_parameters("model/parameters.json")

nd = normal_distribution(xs, standard_deviation, mean)
cdf = cumulative_distribution_function(xs, standard_deviation, mean)

plot_functions(nd, cdf, xs, standard_deviation, mean)


