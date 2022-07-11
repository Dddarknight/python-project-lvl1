#!/usr/bin/env python

from brain_games.launch_games import launch_game
from brain_games.calculations import calc
from brain_games.cli import welcome_user


def main():
    print('brain-calc!' + '\n' + 'Welcome to the Brain Games!')
    name = welcome_user()
    print('What is the result of the expression?')
    launch_game(calc, name)


if __name__ == '__main__':
    main()
