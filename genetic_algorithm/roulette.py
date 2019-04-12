import numpy as np


def chosen_two(valuation):

    chosen = np.random.choice(len(valuation), 2, replace=False, p=valuation)

    return chosen
