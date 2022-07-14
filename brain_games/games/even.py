from random import randint


DESCRIPTION_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def calculate_even():
    number = randint(1, 1000)
    result = 'yes' if is_even(number) else 'no'
    return (str(number), result)
