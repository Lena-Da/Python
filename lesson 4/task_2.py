#Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
#где ключ - значение переданного аргумента, а значение - имя аргумента. 
#Если ключ не хешируем, используйте его строковое представление.


def my_dict(**kwargs):
    result = dict()
    for i, j in kwargs.items():
        if isinstance(j, (list)):
            j = str(j)
        result[j] = i
    return result


print(my_dict(one='22', two='gb', three='-6'))