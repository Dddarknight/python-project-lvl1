#!/usr/bin/env python

from brain_games.launch_games import launch_game
from brain_games.calculations import even


def main():
    launch_game(
        even, 'Answer "yes" if the number is even, otherwise answer "no".')


if __name__ == '__main__':
    main()
