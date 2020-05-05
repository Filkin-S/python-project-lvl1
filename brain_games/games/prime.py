"""Logic for prime number game."""

import random
from math import sqrt

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def play_round():
    number = random.randint(1, 1000)
    answer = 'yes' if is_prime(number) else 'no'
    return number, answer


def is_prime(number):
    if number <= 3:
        return number > 1
    elif number % 2 == 0 or number % 3 == 0:
        return False
    divisor = 5
    sqrt_number = sqrt(number)
    while divisor <= sqrt_number:
        if number % divisor == 0 or number % (divisor + 2) == 0:
            return False
        divisor += 6
    return True
