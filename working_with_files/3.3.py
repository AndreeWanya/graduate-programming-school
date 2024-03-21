from OOP_part_2 import Animal

def objects_creation(filename):
    """ """

    animals = []
    n, flag = 0, 0
    try:
        fi = open(filename, 'rt')
    except FileNotFoundError:
        return (animals, 1)
    for line in fi:
        n += 1
        na = line.rstrip('\n').split(' ')
        try:
            animals.append(Animal(na[0], int(na[1]), float(na[2]), int(na[3]), na[4]))
        except Exception:
            flag = n + 2
            continue
    fi.close()
    return [animals, flag]


animal_list = objects_creation('animals.txt')
errors_list = ['Все ок', 'Файл не найден', 'Следующая строка содержит некорректные данные:']

if animal_list[1] > 2:
    print(errors_list[2], animal_list[1] - 2)
elif animal_list[1] == 1:
    print(errors_list[1])
else:
    for animal in animal_list[0]:
        print(animal.name, animal.speed, animal.animal_says)
