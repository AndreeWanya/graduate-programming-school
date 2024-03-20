from random import randint
import logging


def six_nums_sum(files, my_path):
    result = 0
    for f_name in files:
        with open(my_path + f_name, 'rt') as fi:
            for num in fi:
                try:
                    result += int(num.rstrip())
                except ValueError:
                    print(f'В файле {fi} содержатся некорректные данные.')
                    pass
            fi.close()
    return result


logging.basicConfig(level=logging.INFO, filename='my_log.log', filemode='w', format='%(asctime)s %(levelname)s %(message)s')
num_files = randint(1, 10)
f_names_set = set(str(randint(1, 10)) + '.txt' for x in range(num_files))
logging.info(f"f_names_set equals {f_names_set}")
result = six_nums_sum(f_names_set, 'new_files/')
if result is None:
    print('Ошибка в данных')
else:
    print(result)
