from random import randint


def question_result(game_name):
    if game_name == 'even':
        number = randint(1, 1000)
        if number % 2 == 0:
            result = 'yes'
        else:
            result = 'no'
        return (str(number), result)
    elif game_name == 'calc':
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        choice = randint(1, 3)
        if choice == 1:
            result = number1 + number2
            result_str = f'{number1} + {number2}'
        elif choice == 2:
            result = number1 - number2
            result_str = f'{number1} - {number2}'
        else:
            result = number1 * number2
            result_str = f'{number1} * {number2}'
        return(result_str, str(result))
    elif game_name == 'gcd':
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        result_str = f'{number1} {number2}'
        i = min(number1, number2)
        result = 1
        while i >= 1:
            if (number1 % i == 0) and (number2 % i == 0):
                result = i
                break
            i = i - 1
        return(result_str, str(result))
