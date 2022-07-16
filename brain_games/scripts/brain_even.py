#!/usr/bin/env python

from brain_games.game_engine import start_game
from brain_games.games.even import generate_question_answer_even, DESCRIPTION


def main():
    start_game(generate_question_answer_even, DESCRIPTION)


if __name__ == '__main__':
    main()
