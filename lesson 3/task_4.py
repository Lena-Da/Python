# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

things = {'палатка': 5, 'обувь': 1, 'продукты': 4, 'одежда': 3, 'собака': 10, 'матрас': 6, 'посуда': 3, 'лодка': 10}
bag = int(input('Вместимость рюкзака в кг: '))

for i, j in things.items():
    if j <= bag:
        print(i)
        bag -= j