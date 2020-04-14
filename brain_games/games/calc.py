"""Logic for calculation game."""

import random


def expr_roll():
    ind = random.randint(1, 3)
    num_one = random.randint(1, 100)
    num_two = random.randint(1, 100)
    if ind == 1:
        return '{0} + {1}'.format(num_one, num_two), str(num_one + num_two)
    elif ind == 2:
        return '{0} - {1}'.format(num_one, num_two), str(num_one - num_two)
    return '{0} * {1}'.format(num_one, num_two), str(num_one * num_two)
