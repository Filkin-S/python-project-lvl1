"""Logic for calculation game."""

import operator
import random

RULES = 'What is the result of the expression?'
OPERATIONS = (
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul),
)


def game():
    indicator, operation = random.choice(OPERATIONS)
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    return '{0} {1} {2}'.format(
        number_one, indicator, number_two,
    ), str(operation(number_one, number_two))
