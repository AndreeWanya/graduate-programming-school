class Character:

    def __init__(self, race, name, health, drink, workID):
        self.__race = race        # раса
        self.__name = name        # имя
        self.__HP = health        # здоровье
        self.__drink = drink      # сколько выпито, литры
        self.__workID = workID    # код текущей деятельности: 0 - отдыхает, 1 - выпивает, 2 - работает, 3 - сражается
        
    def get_race(self):
    	return self.__race
    	
    def get_name(self):
    	return self.__name
    	
    def get_health(self):
    	return self.__HP
    	
    def get_drink(self):
    	return self.__drink
    	
    def get_workID(self):
    	return self.__workID
    	
    def set_workID(self, id):
    	self.__workID = id

    def relaxing(self):
        if self.__HP < 10:
            self.__HP += 1
            print('Восстановлено 1 балл здоровья')

    def drinking(self, liter):
        self.__drink += 0.5
        if self.__drink > 5:
            print('Много выпил, че-то поплохело! Надо передохнуть.')
            self.__HP -= 1

    def working(self):
        self.__HP -= 1
        print('1 балл здоровья потерян')

    def fighting(self):
        print(dwarf.__race, dwarf.__name, 'сражается со своими вредными привычками.')

class Weapon:

    def __init__(self, name, material, damage):
        self.__name = name
        self.__material = material
        self.__damage = damage

class Animal:

    def __init__(self, name, kind, mass, speed, animal_says):
        self.__name = name        # кличка
        self.__kind = kind        # тип животного: 1 - кошка, 2 - собака, 3 - попугай
        self.__speed = speed      # 20 для кошки, 15 для собаки, 23 для попугая
        self.__mass = mass        # 10 для кошки, 20 для собаки, 3 для попугая
        self.__animal_says = animal_says      # кошка: "мяу", собака: "гав", попугай: "Вася хороший"

    def get_name(self):
        return self.__name

    def get_animal_says(self):
        return self.__animal_says

    def animal_answer(self):
        print(self.__name, 'говорит:', self.__animal_says)

    def eating(self):
        if self.__kind == 1:
            m = self.__mass * 0.012
        elif self.__kind == 2:
            m = self.__mass * 0.035
        elif self.__kind == 3:
            m = 0.035
        else:
            m = 0
        print(self.__name, 'необходимо', m, 'кг корма в сутки')

    def new_pet_word(self, s):
        self.__animal_says = s


dwarf = Character('дварф', 'Ваня', 10, 0.5, 1)
print('Приветствую, тебя,', dwarf.get_race(), dwarf.get_name() + '!')

for i in range(100):
    if dwarf.get_workID() == 0:
        print(dwarf.get_race(), dwarf.get_name(), 'отдыхает. ')
        dwarf.relaxing()
    elif dwarf.get_workID() == 1:
        print('Выпьем по 0,5')
        dwarf.drinking(0.5)
    elif dwarf.get_workID() == 2:
        print(dwarf.get_race(), dwarf.get_name(), 'работает. Работа отнимает много сил.')
        dwarf.working()
    elif dwarf.get_workID() == 3:
        dwarf.fighting()
    else:
        print('Даже не знаю, чего ты там делаешь.')
    answer = input('Не хотите заняться чем-то другим? д/н, если хотите выйти, введите любой другой символ ')
    if answer == 'д':
        dwarf.set_workID(int(input('Чем сейчас займемся? 0 - отдохнем, 1 - выпьем, 2 - поработаем, 3 - сразимся с кем-нибудь ')))
    elif answer != 'н':
        print('Вы решили нас покинуть! Ждем вас снова!')
        break
    if dwarf.get_health() < 1:
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
print('А теперь', parrot.get_name(), 'умеет говорить:', parrot.get_animal_says())
