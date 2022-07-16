from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    i = number // 2
    while i > 1:
        if number % i == 0:
            return False
        i = i - 1
    return True


def generate_question_answer_prime():
    number = randint(1, 1000)
    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'
    return question, answer
