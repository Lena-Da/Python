# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def fibonacci(num):
    num1, num2 = 1, 1
    print(num1, num2, sep='\n')
    for i in range(num + 1):
        yield num1 + num2
        num1, num2 = num2, num1 + num2
    
print(*fibonacci(5), sep='\n')