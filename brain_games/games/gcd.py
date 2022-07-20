from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def calculate_gcd(number1, number2):
    if number2 == 0:
        return number1
    else:
        return calculate_gcd(number2, number1 % number2)


def generate_round():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = f'{number1} {number2}'
    answer = str(calculate_gcd(number1, number2))
    return question, answer
