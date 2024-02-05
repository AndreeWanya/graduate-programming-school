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


dwarf = Character('дварф', 'Ваня', 10, 0.5, 1)
print('Приветствую, тебя,', dwarf.race, dwarf.name + '!')

for i in range(100):
    if dwarf.workID == 0:
        print(dwarf.race, dwarf.name, 'отдыхает. ')
        dwarf.relaxing()
    elif dwarf.workID == 1:
        print('Выпьем по 0,5')
        dwarf.drinking(0.5)
    elif dwarf.workID == 2:
        print(dwarf.race, dwarf.name, 'работает. Работа отнимает много сил.')
        dwarf.working()
    elif dwarf.workID == 3:
        dwarf.fighting()
    else:
        print('Даже не знаю, чего ты там делаешь.')
    answer = input('Не хотите заняться чем-то другим? д/н, если хотите выйти, введите любой другой символ ')
    if answer == 'д':
        dwarf.workID = int(input('Чем сейчас займемся? 0 - отдохнем, 1 - выпьем, 2 - поработаем, 3 - сразимся с кем-нибудь '))
    elif answer != 'н':
        print('Вы решили нас покинуть! Ждем вас снова!')
        break
    if dwarf.HP < 1:
        print('Вы умерли! До свидания')
        break

cat = Animal('Йося', 1, 3.5, 15, 'мяу')
dog = Animal('Дина', 2, 10, 20, 'гав')
parrot = Animal('Вася', 3, 1, 45, 'Вася хороший')
cat.animal_answer()
cat.eating()
dog.animal_answer()
dog.eating()
parrot.animal_answer()
parrot.eating()

parrot.new_pet_word('Украла кораллы')
print('А теперь', parrot.name, 'умеет говорить:', parrot.animal_says)
