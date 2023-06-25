
"""
Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.

Потренировалась на небольшом задании
За основу взяла своё домашнее задание из семинара 5 про Фибоначчи

"""

class Fibonacci:
    def __init__(self, num):
        self.num = num
        self.num1 = 1
        self.num2 = 1

    def create_fib(self):
        yield self.num1
        yield self.num2
        for i in range(self.num):
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            yield self.num2

f = Fibonacci(5)
print(*f.create_fib(), sep='\n')


'''Исходный код

def fibonacci(num):
    num1, num2 = 1, 1
    print(num1, num2, sep='\n')
    for i in range(num + 1):
        yield num1 + num2
        num1, num2 = num2, num1 + num2
    
print(*fibonacci(5), sep='\n')'''