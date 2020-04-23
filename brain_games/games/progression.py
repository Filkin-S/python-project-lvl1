"""Logic for arithmetic progression game."""

import random

RULES = 'What number is missing in the progression?'


def game():  # noqa: WPS210
    step = random.randint(1, 10)
    number = random.randint(1, 10)
    miss = random.randint(0, 9)
    progression, answer = '', ''
    for counter in range(10):
        if counter == miss:
            answer = str(number)
            chunk = '..'
        else:
            chunk = str(number)
        progression += chunk + ' '  # noqa: WPS336
        number += step
    return progression.rstrip(), answer
