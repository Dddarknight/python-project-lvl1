from random import randint
import operator


DESCRIPTION = 'What is the result of the expression?'
CHOICE = ['+', '-', '*']


def calculate_numbers(number1, number2, operator_choice):
    get_operator = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }.get
    chosen_operator = get_operator(operator_choice)
    return chosen_operator(number1, number2)


def generate_question_answer_calc():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    operator_choice = CHOICE[randint(0, len(CHOICE) - 1)]
    question = f'{number1} {operator_choice} {number2}'
    answer = str(calculate_numbers(number1, number2, operator_choice))
    return question, answer
