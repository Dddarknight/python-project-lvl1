#!/usr/bin/env python

from brain_games.launch_games import launch_game
from brain_games.calculations import gcd


def main():
    launch_game(
        gcd, 'Find the greatest common divisor of given numbers.')


if __name__ == '__main__':
    main()
