import os.path


def check_number(answer, right_answer):
    if answer > right_answer:
        return 'more'
    elif answer < right_answer:
        return 'less'
    elif answer == right_answer:
        return 'equal'


def write_log(text):
    text_lines = ''
    if os.path.exists('log.txt'):
        with open('log.txt', 'r', encoding='utf-8') as open_file:
            lines = open_file.readlines()
            text_lines = ''.join(lines)

    with open('log.txt', 'w', encoding='utf-8') as open_file:
        result = text_lines + text + '\n'
        open_file.write(result)
