from feel_file_random_numbers import feel_numbers
from name_generation_file import name_gen
from mult_pairs_file import two_lines_in_one
from create_file import gen_files
from rename_file import rename_files

if __name__ == '__main__':
    # feel_numbers(3, 'file_1.txt')
    # name_gen(10, 4, 7, 'file_2.txt')
    # two_lines_in_one('file_1.txt', 'file_2.txt', 'result.txt')
    # gen_files('bin', 5, 10, 1024, 4096, 5)
    rename_files('new_name', 3, 'txt', 'doc', [1, 3])