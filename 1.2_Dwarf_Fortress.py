class Main_race:
    race = 'Dwarf'
    name = 'Moradin'
    age = 0
    size = 3000
    career = 'miner'

class Weapon:
    name = 'Battle axe'
    material = 'silver'
    damage = 1

class Animal:
    name = 'bobcat'
    function = 'боевое животное'
    no_gender = False
    exotic = True

dw = Main_race()
print(dw.race + ' ' + dw.name)

elf = Main_race()
elf.race = 'Elf'
elf.name = 'Feanor'
print(elf.race + ' ' + elf.name)

silver_axe = Weapon()
print(silver_axe.name + ', ' + silver_axe.material)

bobcat = Animal()
bobcat.function = 'охотничье животное'
print(bobcat.function + ' ' + bobcat.name)
