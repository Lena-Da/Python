# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

list_double = [1, 2, 3, 1, 2, 4, 5, 7, 8, 5, 2]
list_result = {i for i in list_double if list_double.count(i) > 1}
print(list_result)