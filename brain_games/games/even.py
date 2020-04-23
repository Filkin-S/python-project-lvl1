"""Logic for even number game."""

import random

RULES = 'Answer "yes" if number even otherwise answer "no".'


def game():
    number = random.randint(1, 100)
    return number, 'yes' if is_even(number) else 'no'


def is_even(number):
    if number % 2 == 0:
        return True
    return False
