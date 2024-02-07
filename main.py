from datetime import datetime
from random import randint
import main_functions
import os.path

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
    level = None
    print('Добро пожаловать в игру! \n')
    while level != 0:
        try:
            level = int(input(first_menu))
            if level > 0 and level < 4:
                print(f"Вы выбрали {level_list[level]['name']} уровень сложности \n")
            else:
                print('Выберите уровень от 1 до 3 \n')
        except ValueError:
            print('Введите число! \n')

    right_answer =  randint(0, level_list[level]['max'])
    print('Я загадал число от 0 до ' + level_list[level]['max'] + '. \n')
    answer = None
    answer_count = 0

    while answer!=right_answer:
        try:
            answer = int(input('Какое число я загадал? \n'))
        except ValueError:
            print('Введите число! \n')
