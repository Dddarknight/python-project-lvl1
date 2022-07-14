#!/usr/bin/env python

from brain_games.game_engine import start_game
from brain_games.games.progression import calculate_progression
from brain_games.games.progression import DESCRIPTION_PROGRESSION


def main():
    start_game(calculate_progression, DESCRIPTION_PROGRESSION)


if __name__ == '__main__':
    main()
