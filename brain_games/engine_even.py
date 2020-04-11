"""Main functions for even number game."""

import random

from brain_games.cli import user_answers, welcome_user


def even_check(number):
    if number % 2 == 0:
        return True
    return False


wrong_tmpl = """
"{0}" is wrong answer ;(. Correct answer is {1}.
Let`s try again, {2}!"""


def even_game():
    """Even number game."""
    user_name = welcome_user()
    wins = 0
    while wins < 3:
        number = random.randint(1, 100)
        print('Question: {0}'.format(number))
        answer = user_answers('Your answer: ')
        true_answer = 'yes' if even_check(number) else 'no'
        if answer == true_answer:
            print('Correct!')
            wins += 1
        else:
            print(wrong_tmpl.format(answer, true_answer, user_name))
            break
    if wins == 3:
        print('Congratulations!')
