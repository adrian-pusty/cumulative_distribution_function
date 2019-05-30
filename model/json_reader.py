import json

import numpy as np


def read_parameters_from_json(path):
    try:
        with open(path, "r") as read_file:
            data = json.load(read_file)
            try:
                '''
                    rangeStart and rangeStop must be integers
                    standardDeviation and mean may be integers or floating point numbers
                '''
                return np.array(range(data['rangeStart'], data['rangeStop'])), data['standardDeviation'], data['mean']
            except TypeError:
                print('Wrong json file structure')
    except FileNotFoundError:
        print('No such file like: ' + path)
