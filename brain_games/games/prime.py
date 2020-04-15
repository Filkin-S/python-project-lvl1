"""Logic for prime number game."""

import random


def number_roll():
    number = random.randint(1, 1000)
    answer = 'yes' if is_prime(number) else 'no'
    return number, answer


def is_prime(number):
    if number <= 3:
        return number > 1
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
