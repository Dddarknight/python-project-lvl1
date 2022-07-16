#!/usr/bin/env python

from brain_games.game_engine import start_game
from brain_games.games.progression import generate_question_answer_progression
from brain_games.games.progression import DESCRIPTION


def main():
    start_game(generate_question_answer_progression, DESCRIPTION)


if __name__ == '__main__':
    main()
