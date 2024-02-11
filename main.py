from random import randint
from main_functions import check_number, write_log, datetime


if __name__ == "__main__":
    first_menu = 'Выберите уровень сложности: \n1 - Лёгкий \n2 - Средний \n3 - Тяжелый \nЕсли хотите выйти из игры, нажмите 0 \n'
    level_list = {
        1: {
            'name': 'Легкий',
            'count': 10,
            'max': 15
        },
        2: {
            'name': 'Средний',
            'count': 6,
            'max': 15
        },
        3: {
            'name': 'Тяжелый',
            'count': 3,
            'max': 15
        }
    }

    log_list = {
        'more': [],
        'less': []
    }
    level = None
    print('Добро пожаловать в игру! \n')
    while level != 0:
        try:
            level = int(input(first_menu))
            if level > 0 and level < 4:
                print(f"Вы выбрали {level_list[level]['name']} уровень сложности \n")
                break
            else:
                print('Выберите уровень от 1 до 3 \n')
        except ValueError:
            print('Введите число! \n')

    print(level)
    right_answer = randint(0, level_list[level]['max'])
    print(f"Я загадал число от 0 до {level_list[level]['max']}. Количество попыток: {level_list[level]['count']} \n")
    write_log("[" + str(datetime.now()) + "][INFO][User][System]: Загадано число: " + str(right_answer))
    answer = None
    answer_count = 0

    while answer != right_answer:
        try:
            answer = int(input('Какое число я загадал? \n'))
            answer_count += 1
            check_result, status = check_number(answer, right_answer, answer_count)
            if status != '':
                log_list[status].append(answer)
            write_log(check_result)
            if answer_count == level_list[level]['count']:
                print('Вы проиграли. Количество попыток закончилось')
                break
        except ValueError:
            print('Введите число! \n')

    write_log('Попыток: ' + str(answer_count))
    print(log_list)