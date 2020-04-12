"""Logic for calculation game."""

import random


def expr_roll():
    ind = random.randint(1, 3)
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    if ind == 1:
        return '{0} + {1}'.format(number_one, number_two)
    elif ind == 2:
        return '{0} - {1}'.format(number_one, number_two)
    return '{0} * {1}'.format(number_one, number_two)


def calc_check(expr):
    return str(eval(expr))  # noqa: S307
