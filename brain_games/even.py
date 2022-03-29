import prompt
from random import randint
from brain_games.cli import welcome_user


def even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    while i <= 3:
        number = randint(1, 1000)
        print('Question: ' + str(number))
        answer = prompt.string('Your answer: ')
        if (answer != 'no') and (answer != 'yes'):
            print(str(answer) + " is wrong answer ;(.")
            print("Let's try again, " + name + "!")
            break
        situation1 = (number % 2 == 0) and (answer == 'yes')
        situation2 = (number % 2 != 0) and (answer == 'no')
        if situation1 or situation2:
            print('Correct')
            if i == 3:
                print('Congratulations, ' + name)
            i = i + 1
        else:
            if answer == 'no':
                opposite_answer = 'yes'
            else:
                opposite_answer = 'no'
            text = ' is wrong answer ;(. Correct answer was '
            print(f'{answer}{text}{opposite_answer}')
            print("Let's try again, " + name + "!")
            break
