#!/usr/bin/env python

from brain_games.launch_games import launch_game
from brain_games.calculations import prime
from brain_games.cli import welcome_user


def main():
    print('brain-prime!' + '\n' + 'Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    launch_game(prime, name)


if __name__ == '__main__':
    main()
