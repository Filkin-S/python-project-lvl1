#!/usr/bin/env python3

"""There will be a file desription."""

from brain_games.cli import welcome_user


def greet():
    """Print welcome message."""
    print('Welcome to the Brain Games!')


def main():
    """Execute main script."""
    greet()
    welcome_user()


if __name__ == '__main__':
    main()
