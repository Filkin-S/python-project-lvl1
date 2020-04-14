"""This script executes arithmetic progression game."""

from brain_games.engine import game
from brain_games.games.progression import progress_gen
from brain_games.scripts.brain_games import greet


def game_intro():
    """Print game instruction."""
    print('What number is missing in the progression?')


def main():
    """Execute main even game script."""
    greet()
    game_intro()
    game(progress_gen)


if __name__ == '__main__':
    main()
