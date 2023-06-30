'''Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. 
Напишите к ним классы исключения с выводом подробной информации. Поднимайте исключения внутри основного кода.
Взяла задачу про дроби из ДЗ по второму семинару'''

class FractionError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InputError(FractionError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class CalculationError(FractionError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

try:
    a1, b1 = map(int, input("Первая дробь через /: ").split('/'))
    a2, b2 = map(int, input("Вторая дробь через /: ").split('/'))
    
    if b1 == 0 or b2 == 0:
        raise InputError("Знаментель должен быть больше 0")
    
    if b1 == b2:
        print('{}/{}'.format(a1+a2, b1))
    else:
        b3 = int(b1*b2/gcd(b1, b2))
        a3 = int(b3/b1*a1+b3/b2*a2)
        res = gcd(a3, b3)
        res1 = int(a3/res)
        res2 = int(b3/res)
        print('Сумма {}/{}'.format(res1, res2))

except ValueError:
    raise InputError("Неправильный ввод. Нужно ввести два целых числа, разделённых '/'.")
except InputError as ie:
    print(f"Ошибка ввода: {ie.message}")
except Exception as ex:
    print(f"Ошибка вычислений: {str(ex)}")




'''Задача второго семинара с моим решением:

Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from math import gcd
import fractions

a1, b1 = map(int, input("Первая дробь через /: ").split('/'))
a2, b2 = map(int, input("Вторая дробь через /: ").split('/'))
 
if b1 == b2:
    print('{}/{}'.format(a1+a2, b1))
else:
    b3 = int(b1*b2/gcd(b1, b2))
    a3 = int(b3/b1*a1+b3/b2*a2)
    res = gcd(a3, b3)
    res1 = int(a3/res)
    res2 = int(b3/res)
    print('Сумма {}/{}'.format(res1, res2)) '''