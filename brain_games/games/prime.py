from random import randint


DESCRIPTION_PRIME = (f'Answer "yes" if given number is prime. '
                     f'Otherwise answer "no".')


def calculate_prime():
    number = randint(1, 1000)
    i = number // 2
    result = 'yes'
    number_str = str(number)
    while i > 1:
        if number % i == 0:
            result = 'no'
        i = i - 1
    return (number_str, str(result))
