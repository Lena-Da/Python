
#Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.


import home_work
import random

def generate_queens(n):
    '''
    случайная расстановка ферзей на доске
    '''
    queens_new = []
    for i in range(n):
        queens_new.append((i, random.randint(0, n-1)))
    return queens_new

successful_arrangements = []
while len(successful_arrangements) < 4:
    queens_new = generate_queens(8)
    if home_work.check_queens(queens_new):
        successful_arrangements.append(queens_new)
        print("Успешная расстановка:", queens_new)  