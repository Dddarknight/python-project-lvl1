import prompt
from brain_games.cli import welcome_user


MAX_ATTEMPTS_COUNT = 3


def start_game(calculate_result,
               game_description,
               max_attempts_count=MAX_ATTEMPTS_COUNT):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(game_description)
    attempt_number = 1
    while attempt_number <= max_attempts_count:
        (question, expected_answer) = calculate_result()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != expected_answer:
            print(f'{answer} is wrong answer ;(. Correct answer was '
                  f'{expected_answer}\n'
                  f"Let's try again, {name}!")
            return
        print('Correct')
        attempt_number += 1
    print(f'Congratulations, {name}!')
