from random import randint

def six_nums_sum(n, m, my_path):
    result = 0
    with open(my_path + str(n) + '.txt', 'rt') as fi:
        for num in fi:
            try:
                result += int(num.rstrip())
            except ValueError:
                return None
        fi.close()
    with open(my_path + str(m) + '.txt', 'rt') as fi:
        for num in fi:
            try:
                result += int(num.rstrip())
            except ValueError:
                return None
        fi.close()
    return result

n, m = randint(1, 10), randint(1, 10)
result = six_nums_sum(n, m, 'new_files/')
if result == None:
    print('Ошибка в данных')
else:
    print(result)
