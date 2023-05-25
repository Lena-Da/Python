# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.


def task2(num, system):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = alphabet[num % system] 
    while num >= system :
        num = num // system
        b += alphabet[num % system] 
    print("0x", b[::-1])

task2(76, 16)    
print(hex(76)) 
