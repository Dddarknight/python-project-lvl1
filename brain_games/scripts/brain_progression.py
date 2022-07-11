#!/usr/bin/env python

from brain_games.launch_games import launch_game
from brain_games.calculations import progression
from brain_games.cli import welcome_user


def main():
    print('brain-progression!' + '\n' + 'Welcome to the Brain Games!')
    name = welcome_user()
    print('What number is missing in the progression?')
    launch_game(progression, name)


if __name__ == '__main__':
    main()
