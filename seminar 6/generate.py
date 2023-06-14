"""
2/Создайте модуль с функцией внутри. 
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток. 
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток. 
Функция выводит подсказки “больше” и “меньше”. 
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

"""
import random as rnd

def gen_fnc(low: int = 1, hight: int = 50, try_count: int = 5) -> bool:
    result = False
    num = rnd.randint(low, hight + 1)
    search_count = 0
    while search_count < try_count:
        ask_value = int(input(f'input num at {low} to {hight}: '))
        if ask_value == num:
            print('вы угадали ')
            result = True
            break
        if ask_value < num:
            print('число больше ')
        else:
            print('число меньше ')
        search_count += 1
    else:
        print('попытки закончились')

    return result