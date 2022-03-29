import prompt
from brain_games.cli import welcome_user
from brain_games.calculations import question_result


def first_question(game_name):
    if game_name == 'even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif game_name == 'calc':
        print('What is the result of the expression?')
    elif game_name == 'gcd':
        print('Find the greatest common divisor of given numbers.')


def game(game_name):
    name = welcome_user()
    first_question(game_name)
    i = 1
    while i <= 3:
        (question, result) = question_result(game_name)
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if (game_name == 'even') and (answer != 'no') and (answer != 'yes'):
            print(str(answer) + " is wrong answer ;(.")
            print("Let's try again, " + name + "!")
            break
        if answer != result:
            text = ' is wrong answer ;(. Correct answer was '
            print(f'{answer}{text}{result}')
            print("Let's try again, " + name + "!")
            break
        else:
            print('Correct')
            if i == 3:
                print('Congratulations, ' + name)
            i = i + 1
