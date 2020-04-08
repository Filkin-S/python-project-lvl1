"""There will be a file desription."""

import prompt


def welcome_user():
    """Greet user."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
