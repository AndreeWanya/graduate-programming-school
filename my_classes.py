class Car():
    """ Любой автомобиль """

    def __init__(self, maker, model, year):
        self._maker = maker
        self._model = model
        self._year = year

    def get_full_name(self):
        full_name = f"{self._maker} {self._model} {self._year}"
        return full_name


class ElectricCar(Car):
    """ Электромобиль """

    def __init__(self, maker, model, year, battery_size):
        super().__init__(maker, model, year)
        self.__battery_size = battery_size

    def set_battery_size(self, b_size):
        self.__battery_size = b_size

    def get_battery_size(self):
        return self.__battery_size


class Lorry(Car):
    """ Грузовик """

    def __init__(self, maker, model, year):
        super().__init__(maker, model, year)
        self.__tonnage = 15

    def set_tonnage(self, ton):
        self.__tonnage = ton

    def get_tonnage(self):
        return self.__tonnage


class Bus(Car):
    """ Автобюус """

    def __init__(self, maker, model, year, seats):
        super().__init__(maker, model, year)
        self.__seats = seats

    def get_seats(self):
        return self.__seats

    def set_seats(self, pass_seats):
        self.__seats = pass_seats

PAZ_32054 = Bus('Павловский автобусный завод', "ПАЗ-32054", 2023, 39)
Kamaz_65115 = Lorry('Камский автомобильный завод', "КамАЗ-65115", 2011)
my_wife_car = ElectricCar('Nissan', 'Leaf', 2015, 75)

print(f'Моя жена ездит на {my_wife_car.get_full_name()}')
print(f'Вчера я ехал на работу на автобусе {PAZ_32054._model}. Все {PAZ_32054.get_seats()} сиденья были заняты.')
print(f'На карьере работает {Kamaz_65115._model}, грузоподъемностью {Kamaz_65115.get_tonnage()} тонн.')
