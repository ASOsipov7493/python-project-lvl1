#!/usr/bin/env python

"""The scripts start the game 'Brain-prime'"""

from brain_games.engine import engine
from brain_games.games import prime_numbers


def main():
    """
    Program start.
    Parameters are missing.
    Returns: None
    """
    engine(prime_numbers)


if __name__ == '__main__':
    main()
