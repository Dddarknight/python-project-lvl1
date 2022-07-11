#!/usr/bin/env python

from brain_games.launch_games import launch_game
from brain_games.calculations import even
from brain_games.cli import welcome_user


def main():
    print('brain-even!' + '\n' + 'Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    launch_game(even, name)


if __name__ == '__main__':
    main()
