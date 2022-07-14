#!/usr/bin/env python

from brain_games.game_engine import start_game
from brain_games.games.calc import calculate_numbers, DESCRIPTION_CALC


def main():
    start_game(calculate_numbers, DESCRIPTION_CALC)


if __name__ == '__main__':
    main()
