# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def task1(path: str):
    result = path.split('/')
    name, type_file = result[3].split('.')
    res='/'.join(result[:3])
    return res, name, type_file

print(task1('C:/lena/lesson1/task_1.py'))