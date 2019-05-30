from model.json_reader import read_parameters_from_json
from controller.formula_to_df import cumulative_distribution_function, normal_distribution
from view.view import plot_functions

xs, standard_deviation, mean = read_parameters_from_json("model/parameters.json")

nd = normal_distribution(xs, standard_deviation, mean)
cdf = cumulative_distribution_function(xs, standard_deviation, mean)

plot_functions(nd, cdf, xs, standard_deviation, mean)


