#!/usr/bin/env python

from brain_games.launch_games import launch_game
from brain_games.calculations import prime


def main():
    launch_game(
        prime, 'Answer "yes" if given number is prime. Otherwise answer "no".')


if __name__ == '__main__':
    main()
