'''Домашнее задание
Напишите функцию группового переименования файлов. Она должна:
принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
принимать параметр количество цифр в порядковом номере.
принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
принимать параметр расширение конечного файла.
принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение'''

import os

def rename_files(new_name, number_digits, file_extension, new_extension, name_range=None):
    file_counter = 1
    for filename in os.listdir('.'):
        if filename.endswith(file_extension):
            if name_range is not None:
                orig_name = filename[name_range[0]-1:name_range[1]]
            else:
                orig_name = filename[:len(filename)-len(file_extension)]
            if new_name is not None:
                new_filename = new_name + '_' + str(file_counter).zfill(number_digits) + '.' + new_extension
            else:
                new_filename = orig_name + '_' + str(file_counter).zfill(number_digits) + '.' + new_extension
            os.rename(filename, new_filename)
            file_counter += 1
