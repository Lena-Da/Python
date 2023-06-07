#Напишите функцию для транспонирования матрицы

def matrix_transp(matrix):
    new_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print('Транспонированная матрица', *new_matrix, sep='\n')

matrix = [[1,2,3], [4,5,6], [7,8,9]]
print('Исходная матрица', *matrix, sep='\n')     
matrix_transp(matrix)
