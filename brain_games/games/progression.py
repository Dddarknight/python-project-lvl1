from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def make_random_progression():
    progression_length = randint(5, 10)
    progression_first_number = randint(1, 100)
    progression_step = randint(1, 10)
    current_element = progression_first_number
    progression_elements = []
    for i in range(0, progression_length):
        progression_elements.append(current_element)
        current_element += progression_step
    return progression_elements


def generate_question_answer_progression():
    progression_elements = make_random_progression()
    missing_index = randint(0, len(progression_elements) - 1)
    answer = str(progression_elements[missing_index])
    progression_elements[missing_index] = '..'
    progression_elements_str = [str(elem) for elem in progression_elements]
    question = ' '.join(progression_elements_str).strip()
    return question, answer
