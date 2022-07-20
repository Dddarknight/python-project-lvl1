from random import randint
import operator


DESCRIPTION = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']
MAP_SIGN_TO_OPERATION = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def calculate(number1, number2, chosen_operator):
    chosen_operation = MAP_SIGN_TO_OPERATION[chosen_operator]
    return chosen_operation(number1, number2)


def generate_round():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    chosen_operator = OPERATORS[randint(0, len(OPERATORS) - 1)]
    question = f'{number1} {chosen_operator} {number2}'
    answer = str(calculate(number1, number2, chosen_operator))
    return question, answer
