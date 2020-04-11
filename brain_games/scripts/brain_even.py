"""This script executes even number brain game ."""

from brain_games.engine_even import even_game
from brain_games.scripts.brain_games import greet


def game_intro():
    """Print game instruction."""
    print('Answer "yes" if number even otherwise answer "no".')


def main():
    """Execute main even game script."""
    greet()
    game_intro()
    even_game()


if __name__ == '__main__':
    main()
