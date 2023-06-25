'''Задание №5
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.

Задание №6
Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения'''


class Rectangle:
    '''Класс прямоугольник, с методами расчета периметра и площади фигуры.'''

    def __init__(self, a: int, b: int = None):
        '''Метод инициализации прямоугольника со сторонами a и b.'''
        self.a = a
        self.b = b if b is not None else a

    def area(self) -> int:
        '''Метод расчета площади прямоугольника.'''
        return self.a * self.b
    
    def perimeter(self) -> int:
        '''Метод расчета периметра прямоугольника.'''
        return 2 * (self.a + self.b)
    
    def __add__(self, other):
        '''Переопределенный дандер метод сложения двух прямоугольников.'''
        new_perimeter = self.perimeter() + other.perimeter()
        new_a = self.a
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)
    
    def __sub__(self, other):
        '''Переопределенный дандер метод вычитания двух прямоугольников.'''
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_a = min([self.a, self.b, other.a, other.b])
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)
    
    def __str__(self):
        '''Переопределенный дандер метод строчного выведения экземпляра класса'''
        return f'Прямоугольник {self.a} x {self.b}'
    
    def print_info(self):
        '''Метод вывода информации о прямоугольнике на печать.'''
        print(f'Стороны прямоугольника: {self.a} x {self.b}')
        print(f'Площадь прямоугольника: {self.area()}')
        print(f'Периметр прямоугольника: {self.perimeter()}')

    def __eq__(self, other):
        '''Переопределенный дандер метод сравнения двух прямоугольников по площади.'''
        return self.area() == other.area()
    
    def __ne__(self, other):
        '''Переопределенный дандер метод сравнения двух прямоугольников по площади.'''
        return self.area() != other.area()
    
    def __lt__(self, other):
        '''Переопределенный дандер метод сравнения двух прямоугольников по площади.'''
        return self.area() < other.area()
    
    def __le__(self, other):
        '''Переопределенный дандер метод сравнения двух прямоугольников по площади.'''
        return self.area() <= other.area()
    
    def __gt__(self, other):
        '''Переопределенный дандер метод сравнения двух прямоугольников по площади.'''
        return self.area() > other.area()
    
    def __ge__(self, other):
        '''Переопределенный дандер метод сравнения двух прямоугольников по площади.'''
        return self.area() >= other.area()

    
if __name__ == '__main__':
    rect_1 = Rectangle(2, 5)
    rect_2 = Rectangle(5, 10)
    print(rect_2)
    rect_1.print_info()
    rect_2.print_info()
    #print(f'{rect1.area()=} {rect1.perimetr()=}')
    #print(f'{rect2.area()=} {rect2.perimetr()=}')
    res_sum = rect_1 + rect_2
    res_sum.print_info()
    res_sub = rect_1 - rect_2
    res_sub.print_info()

    print(rect_1 == rect_2)
    print(rect_1 != rect_2)
    print(rect_1 < rect_2)
    print(rect_1 <= rect_2)
    print(rect_1 > rect_2)
    print(rect_1 >= rect_2)