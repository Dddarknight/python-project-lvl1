from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(progression_length,
                         progression_first_number,
                         progression_step):
    progression_elements = []
    for i in range(0, progression_length):
        current_element = progression_first_number + i * progression_step
        progression_elements.append(current_element)
    return progression_elements


def generate_question(progression_elements, missing_element_index):
    progression_elements[missing_element_index] = '..'
    progression_elements_str = [str(elem) for elem in progression_elements]
    question = ' '.join(progression_elements_str).strip()
    return question


def generate_round():
    progression_length = randint(5, 10)
    progression_first_number = randint(1, 100)
    progression_step = randint(1, 10)
    progression_elements = generate_progression(progression_length,
                                                progression_first_number,
                                                progression_step)
    missing_element_index = randint(0, len(progression_elements) - 1)
    answer = str(progression_elements[missing_element_index])
    question = generate_question(progression_elements, missing_element_index)
    return question, answer
