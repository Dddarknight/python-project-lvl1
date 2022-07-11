import prompt


def launch_game(func_game, name):
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
        if i == 3:
            print('Congratulations, ' + name + '!')
        i = i + 1
