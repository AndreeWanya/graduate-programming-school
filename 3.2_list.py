from random import randint
import logging


def six_nums_sum(files, my_path):
    result, flag = 0, 0
    for f_name in files:
        try:
            fi = open(my_path + f_name, 'rt')
        except FileNotFoundError:
            return [result, 1]
        lines = fi.readlines()
        if len(lines) != 3:
            return [result, 2]
        for line in lines:
            try:
                result += int(line.rstrip())
            except ValueError:
                flag = 3
    return [result, flag]


logging.basicConfig(level=logging.INFO, filename='my_log.log', filemode='w', format='%(asctime)s %(levelname)s %(message)s')
num_files = randint(1, 10)
f_names_set = set(str(randint(1, 10)) + '.txt' for x in range(num_files))
logging.info(f"f_names_set equals {f_names_set}")
result = six_nums_sum(f_names_set, 'new_files/')
error_results = ['Ошибок нет', 'Один из файлов не найден', 'Файл содержит больше/меньше строк, чем должен', 'Невозможно обработать строку']

print(error_results[result[1]])
print(result[0])
