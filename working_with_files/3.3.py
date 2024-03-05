from OOP_part_2 import Animal

def objects_creation(filename):
    animals = []
    n = 0
    with open(filename, 'rt') as fi:
        for line in fi:
            n += 1
            na = line.rstrip('\n').split(' ')
            try:
                animals.append(Animal(na[0], int(na[1]), float(na[2]), int(na[3]), na[4]))
            except Exception:
                print(n, 'строка содержит некорректные данные!')
        fi.close()
    return animals

animal_list = objects_creation('animals.txt')

print(animal_list[0].name)
print(animal_list[1].speed)
print(animal_list[2].animal_says)


