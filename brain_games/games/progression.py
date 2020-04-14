"""Logic for arithmetic progression game."""

import random


def progress_gen():  # noqa: WPS210
    step = random.randint(1, 10)
    number = random.randint(1, 10)
    miss = random.randint(0, 9)
    progression, answer = '', ''
    for counter in range(9):
        if counter == miss:
            answer = str(number)
            progression = '{0}.. '.format(progression)
            number += step
        progression += '{0} '.format(str(number))
        number += step
    return progression, answer
