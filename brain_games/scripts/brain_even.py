"""This script executes even number brain game ."""

from brain_games.engine import game
from brain_games.games.even import number_roll
from brain_games.scripts.brain_games import greet


def game_intro():
    """Print game instruction."""
    print('Answer "yes" if number even otherwise answer "no".')


def main():
    """Execute main even game script."""
    greet()
    game_intro()
    game(number_roll)


if __name__ == '__main__':
    main()
