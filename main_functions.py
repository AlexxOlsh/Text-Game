from datetime import datetime
import os.path

def check_number(answer, right_answer):
    current_dt = datetime.now()
    if answer > right_answer:
        result = "[" + str(current_dt) + "][INFO][User]: Введено число " + str(answer)
        print('Не угадали. Число должно быть меньше')
        return result
    elif answer < right_answer:
        result = "[" + str(current_dt) + "][INFO][User]: Введено число " + str(answer)
        print('Не угадали. Число должно быть больше')
        return result
    elif answer == right_answer:
        result = "[" + str(current_dt) + "][INFO][User][System]: Число угадано."
        print('Поздравляю! Вы угадали!')
        return result


def write_log(text):
    text_lines = ''
    if os.path.exists('log.txt'):
        with open('log.txt', 'r', encoding='utf-8') as open_file:
            lines = open_file.readlines()
            text_lines = ''.join(lines)
            print(text_lines)

    with open('log.txt', 'w', encoding='utf-8') as open_file:
        result = text_lines + text + '\n'
        open_file.write(result)
