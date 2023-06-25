'''Создайте класс Матрица. Добавьте методы для:
вывода на печать,
сравнения,
сложения'''


class Matrix:
    '''Класс для представления матрицы.'''
    

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for j in range(cols)] for i in range(rows)]

    def __str__(self):
        '''Метод для вывода матрицы на печать.'''
        res = ""
        for i in range(self.rows):
            for j in range(self.cols):
                res += str(self.data[i][j]) + " "
            res += "\n"
        return res

    def __eq__(self, other):
        '''Метод для сравнения матриц.'''
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        '''Метод для сложения матриц.'''
        res = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                res.data[i][j] = self.data[i][j] + other.data[i][j]
        return res


matrix1 = Matrix(3, 3)
matrix2 = Matrix(3, 3)

for i in range(3):
    for j in range(3):
        matrix1.data[i][j] = i + j
        matrix2.data[i][j] = i - j

print("Матрица1:")
print(matrix1)
print("Матрица2:")
print(matrix2)

if matrix1 == matrix2:
    print("Матрицы равны")
else:
    print("Матрицы не равны")

sum_matrix = matrix1 + matrix2
print("Сумма матриц:")
print(sum_matrix)

