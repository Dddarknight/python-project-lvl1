from random import randint


def even():
    number = randint(1, 1000)
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return (str(number), result)


def calc():
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
    return (result_str, str(result))


def gcd():
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


def progression():
    pro_length = randint(5, 10)
    pro_begin = randint(1, 100)
    pro_step = randint(1, 10)
    miss_position = randint(0, pro_length - 1)
    i = 0
    next = pro_begin
    pr_str = str(next)
    miss_begin = 0
    miss_end = 0 + len(str(next))
    while i <= pro_length - 1:
        if i == miss_position:
            result = str(next)
            miss_begin = len(pr_str) - 1 - (len(str(next)) - 1)
            miss_end = miss_begin + len(str(next)) - 1
        if i != pro_length - 1:
            next = next + pro_step
            pr_str = pr_str + ' ' + str(next)
        i = i + 1
    result_str = pr_str[:miss_begin] + '..' + pr_str[miss_end + 1:]
    return(result_str, str(result))


def prime():
    number = randint(1, 1000)
    i = number // 2
    result = 'yes'
    result_str = str(number)
    while i > 1:
        if number % i == 0:
            result = 'no'
        i = i - 1
    return(result_str, str(result))
