"""Logic for even number game."""

import random


def number_roll():
    number = random.randint(1, 100)
    return number, even_check(number)


def even_check(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'
