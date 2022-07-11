#!/usr/bin/env python

from brain_games.launch_games import launch_game
from brain_games.calculations import calc


def main():
    launch_game(
        calc, 'What is the result of the expression?')


if __name__ == '__main__':
    main()
