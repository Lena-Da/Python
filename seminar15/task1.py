'''Возьмите любые 1-3 задачи из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации. 
Также реализуйте возможность запуска из командной строки с передачей параметров.'''

'''Взяла задание №1 из семинара 13
Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
Обрабатывайте не числовые данные как исключения.'''


import logging
import sys

def num_exc():
    while True:
        if len(sys.argv) > 1:
            num = sys.argv[1]
        else:
            num = input('Введите целое или вещественное число: ')
        try:
            num = int(num)
            break
        except ValueError as e:
            try:
                num = float(num)
                break
            except ValueError as e:
                logging.error(f'Ошибка при вводе числа: {e}')
                print(f'Вы ввели неправильное значение: {e}\nПопробуйте снова!')
    return num

if __name__ == '__main__':
    logging.basicConfig(filename='log.log', level=logging.ERROR, encoding='UTF-8')
    
    print(type(num_exc()))