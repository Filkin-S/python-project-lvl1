"""This script executes greatest common divisor brain game."""

from brain_games.engine import game
from brain_games.games.gcd import gcd_numbers
from brain_games.scripts.brain_games import greet


def game_intro():
    """Print game instruction."""
    print('Find the greatest common divisor of given numbers.')


def main():
    """Execute main even game script."""
    greet()
    game_intro()
    game(gcd_numbers)


if __name__ == '__main__':
    main()
