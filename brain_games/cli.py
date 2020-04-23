"""Command Line Interface functions."""

import prompt


def welcome_user():
    """Greets, asks and return users name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def ask(input_text):
    user_answer = prompt.string(input_text)
    return user_answer
