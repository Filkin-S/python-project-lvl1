"""This script executes even number brain game ."""

from brain_games.engine import game
from brain_games.games.calc import calc_check, expr_roll
from brain_games.scripts.brain_games import greet


def game_intro():
    """Print game instruction."""
    print('What is the result of the expression?')


def main():
    """Execute main calculation game script."""
    greet()
    game_intro()
    game(expr_roll, calc_check)


if __name__ == '__main__':
    main()
