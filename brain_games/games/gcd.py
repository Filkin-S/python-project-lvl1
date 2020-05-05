"""Logic for greatest common divisor game."""

import random

RULES = 'Find the greatest common divisor of given numbers.'


def play_round():
    num_one = random.randint(1, 100)
    num_two = random.randint(1, 100)
    return '{0} {1}'.format(num_one, num_two), str(find_gcd(num_one, num_two))


def find_gcd(first_num, second_num):
    while second_num:
        first_num, second_num = second_num, first_num % second_num
    return first_num
