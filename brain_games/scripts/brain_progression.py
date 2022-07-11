#!/usr/bin/env python

from brain_games.launch_games import launch_game
from brain_games.calculations import progression


def main():
    launch_game(
        progression, 'What number is missing in the progression?')


if __name__ == '__main__':
    main()
