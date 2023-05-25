# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

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
    print('Сумма {}/{}'.format(res1, res2)) 

'''
f1 = fractions.Fraction(1, 3)
f2 = fractions.Fraction(4, 5)
print(f1 + f2)
'''
