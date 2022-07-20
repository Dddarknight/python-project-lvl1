from random import randint
import math


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def generate_round():
    number = randint(1, 1000)
    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'
    return question, answer
