"""
4/ Создайте модуль с функцией внутри. 
Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

5/ Добавьте в модуль с загадками функцию, которая хранит словарь списков. 
Ключ словаря - загадка, значение - список с отгадками. 
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки. 

"""

def puzzle(text: str, answers: list[str], try_count: int) -> int:
    print(text)
    count_trying = 1


    while count_trying <= try_count:
        answer = input('What is it: ')
        if answer in answers:
            break
        count_trying += 1
        if count_trying != try_count:
            print('Не угадал, еще одна попытка')
        count_trying += 1
    else:
        count_trying = 0

    return count_trying