class Character:

    def __init__(self, race, name, health, drink, workID):
        self.race = race        # раса
        self.name = name        # имя
        self.HP = health        # здоровье
        self.drink = drink      # сколько выпито, литры
        self.workID = workID    # код текущей деятельности: 0 - отдыхает, 1 - выпивает, 2 - работает, 3 - сражается

    def relaxing(self):
        if self.HP < 10:
            self.HP += 1
            print('Восстановлено 1 балл здоровья')

    def drinking(self, liter):
        self.drink += 0.5
        if self.drink > 5:
            print('Много выпил, че-то поплохело! Надо передохнуть.')
            self.HP -= 1

    def working(self):
        self.HP -= 1
        print('1 балл здоровья потерян')

    def fighting(self):
        print(dwarf.race, dwarf.name, 'сражается со своими вредными привычками.')

class Weapon:

    def __init__(self, name, material, damage):
        self.name = name
        self.material = material
        self.damage = damage

class Animal:

    def __init__(self, name, kind, mass, speed, animal_says):
        self.name = name        # кличка
        self.kind = kind        # тип животного: 1 - кошка, 2 - собака, 3 - попугай
        self.speed = speed      # 20 для кошки, 15 для собаки, 23 для попугая
        self.mass = mass        # 10 для кошки, 20 для собаки, 3 для попугая
        self.animal_says = animal_says      # кошка: "мяу", собака: "гав", попугай: "Вася хороший"

    def animal_answer(self):
        print(self.name, 'говорит:', self.animal_says)

    def eating(self):
        if self.kind == 1:
            m = self.mass * 0.012
        elif self.kind == 2:
            m = self.mass * 0.035
        elif self.kind == 3:
            m = 0.035
        else:
            m = 0
        print(self.name, 'необходимо', m, 'кг корма в сутки')

    def new_pet_word(self, s):
        self.animal_says = s
