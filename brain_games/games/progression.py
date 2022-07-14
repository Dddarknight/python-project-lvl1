from random import randint


DESCRIPTION_PROGRESSION = 'What number is missing in the progression?'


def calculate_progression():
    progression_length = randint(5, 10)
    progression_first_number = randint(1, 100)
    progression_step = randint(1, 10)
    miss_position = randint(0, progression_length - 1)
    i = 0
    next_number = progression_first_number
    str_accumulative = str(next_number)
    miss_begin_position = 0
    miss_end_position = 0 + len(str(next_number))
    while i <= progression_length - 1:
        if i == miss_position:
            result = str(next_number)
            miss_begin_position = len(str_accumulative) - len(str(next_number))
            miss_end_position = miss_begin_position + len(str(next_number)) - 1
        if i != progression_length - 1:
            next_number = next_number + progression_step
            str_accumulative += f' {str(next_number)}'
        i += 1
    progression_str = (f'{str_accumulative[:miss_begin_position]}..'
                       f'{str_accumulative[miss_end_position + 1:]}')
    return (progression_str, str(result))
