# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии

def bonus():

    names = ['Robert', 'Tom', 'Henry']
    salaries = [15000, 20000, 30000]
    bonuses = ['10.25%', '5.15%', '15.10%']

    print({name: (salary * float(bonus[:-1]) / 100) for name, salary, bonus in zip(names, salaries, bonuses)})

bonus()