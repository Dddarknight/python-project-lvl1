from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def calculate_gcd(number1, number2):
    minimum = min(number1, number2)
    result = 1
    while minimum >= 1:
        if (number1 % minimum == 0) and (number2 % minimum == 0):
            result = minimum
            break
        minimum -= 1
    return result


def generate_question_answer_gcd():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = f'{number1} {number2}'
    answer = str(calculate_gcd(number1, number2))
    return question, answer
