"""This script executes calculation brain game ."""

from brain_games import engine, games


def main():
    """Execute main calculation game script."""
    engine.run(games.calc)


if __name__ == '__main__':
    main()
