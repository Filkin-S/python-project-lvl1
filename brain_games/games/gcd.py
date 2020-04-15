"""Logic for greatest common divisor game."""

import random


def gcd_numbers():
    num_one = random.randint(1, 100)
    num_two = random.randint(1, 100)
    return '{0} {1}'.format(num_one, num_two), str(gcd(num_one, num_two))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
