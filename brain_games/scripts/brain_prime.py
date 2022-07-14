#!/usr/bin/env python

from brain_games.game_engine import start_game
from brain_games.games.prime import calculate_prime, DESCRIPTION_PRIME


def main():
    start_game(calculate_prime, DESCRIPTION_PRIME)


if __name__ == '__main__':
    main()
