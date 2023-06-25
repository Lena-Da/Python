'''Вторая доработанная задача по второму заданию из семинара 10
Потренировалась, на небольшом задании
За основу взяла задание 3 из семинара 7, там где складывали числа и строки из разынх файлов в один
'''
from typing import TextIO
from pathlib import Path


class MultPairsFile:
    def __init__(self, numbers_path: Path, words_path: Path, result_path: Path):
        self.numbers_path = numbers_path
        self.words_path = words_path
        self.result_path = result_path

    def _read_or_begin(self, fd: TextIO) -> str:
        line = fd.readline()
        if not line:
            fd.seek(0)
            return self._read_or_begin(fd)
        return line[:-1]

    def two_lines_in_one(self) -> None:
        with open(self.numbers_path, 'r', encoding='utf-8') as f_num, \
             open(self.words_path, 'r', encoding='utf-8') as f_word, \
             open(self.result_path, 'w', encoding='utf-8') as f_res:
            len_numbers = sum(1 for _ in f_num)
            len_word = sum(1 for _ in f_word)
            for _ in range(max(len_numbers, len_word)):
                num = self._read_or_begin(f_num)
                word = self._read_or_begin(f_word)
                num_a, num_b = num.split('|')
                mult = int(num_a) * float(num_b)
                if mult < 0:
                    f_res.write(f'{word.lower()}{abs(mult)}\n')
                elif mult > 0:
                    f_res.write(f'{word.upper()}{round(mult)}\n')


numbers_path = Path('numbers.txt')
words_path = Path('words.txt')
result_path = Path('result.txt')

result = MultPairsFile(numbers_path, words_path, result_path)
result.two_lines_in_one()


'''def _read_or_begin(fd: TextIO) -> str:
    line = fd.readline()
    if not line:
        fd.seek(0)
        return _read_or_begin(fd)
    return line[:-1]

def two_lines_in_one(numbers: Path, words: Path, result: Path) -> None:
    with(open(numbers, 'r', encoding='utf-8') as f_num,
         open(words, 'r', encoding='utf-8') as f_word,
         open(result, 'w', encoding='utf-8') as f_res
         ):
        len_numbers = sum(1 for _ in f_num)
        len_word = sum(1 for _ in f_word)
        for _ in range(max(len_numbers, len_word)):
            num = _read_or_begin(f_num)
            word = _read_or_begin(f_word)
            num_a, num_b = num.split('|')
            mult = int(num_a) * float(num_b)
            if mult < 0:
                f_res.write(f'{word.lower()}{abs(mult)}\n')
            elif mult > 0:
                f_res.write(f'{word.upper()}{round(mult)}\n')'''