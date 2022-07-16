#!/usr/bin/env python

from brain_games.game_engine import start_game
from brain_games.games.prime import generate_question_answer_prime, DESCRIPTION


def main():
    start_game(generate_question_answer_prime, DESCRIPTION)


if __name__ == '__main__':
    main()
