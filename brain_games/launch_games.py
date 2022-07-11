import prompt
from brain_games.cli import welcome_user


def launch_game(func_game, question):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(question)
    i = 1
    while i <= 3:
        (question, result) = func_game()
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if answer != result:
            text = ' is wrong answer ;(. Correct answer was '
            print(f'{answer}{text}{result}')
            print("Let's try again, " + name + "!")
            break
        else:
            print('Correct')
        i = i + 1
    if i == 4:
        print('Congratulations, ' + name + '!')
