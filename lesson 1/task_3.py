# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:

from random import randint
num = randint(1, 10)
print('Угадайте число от 1 до 10, у вас есть 10 попыток')

count = 0
while count < 10:
    answer = int(input('Ваш вариант: '))
    count += 1
    print('Это {0} попытка'.format(count))
    if answer < num:
        print('Число больше вашего')
    elif answer > num:
        print ('Число меньше вашего')    

if answer == num:
    print ('Вы угадали')
else:
    print ('Попытки закончились')