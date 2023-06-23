'''Напишите следующие функции:
Нахождение корней квадратного уравнения <br>
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.<br>
Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.<br>
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.<br>'''

import csv
import json
import random
from functools import wraps
from typing import Tuple


def find_roots(a: float, b: float, c: float) -> Tuple[float, float]:
    '''Нахождение корней квадратного уравнения'''
    res = b ** 2 - 4 * a * c
    if res < 0:
        raise ValueError("Корней нет")
    elif res == 0:
        x = -b / (2 * a)
        return x, x
    else:
        x1 = (-b + res ** 0.5) / (2 * a)
        x2 = (-b - res ** 0.5) / (2 * a)
        return x1, x2


def create_csv(filename: str, rows: int):
    '''Генерация csv файла с тремя случайными числами в каждой строке'''
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for i in range(rows):
            row = [random.uniform(-10, 10) for _ in range(3)]
            writer.writerow(row)


def roots_csv(func):
    '''Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла'''
    @wraps(func)
    def wrapper(filename: str):
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    a, b, c = map(float, row)
                    result = func(a, b, c)
                    print(f"Корни уравнения {a}x^2 + {b}x + {c}:", result)
                except ValueError as e:
                    print(e)
    return wrapper


def create_json(func):
    '''Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        data = {"args": args,"kwargs": kwargs,"result": result}
        with open(f"{func.__name__}.json", mode='w') as file:
            json.dump(data, file, indent=4)
        return result
    return wrapper


create_csv("file.csv", 100)

@roots_csv
def find_roots_csv(a: float, b: float, c: float) -> Tuple[float, float]:
    return find_roots(a, b, c)

find_roots_csv("file.csv")

@create_json
def json_file(x: float, y: float) -> float:
    return x + y

json_file(2, 3)
