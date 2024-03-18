class Car():
    """ Любой автомобиль """

    def __init__(self, maker, model, year):
        self._maker = maker
        self._model = model
        self._year = year
        self._engine = Engine(1)

    def get_full_name(self):
        full_name = f"{self._maker} {self._model} {self._year}"
        return full_name

    def get_engine(self):
        return self._engine


class ElectricCar(Car):
    """ Электромобиль """

    def __init__(self, maker, model, year, battery_size):
        super().__init__(maker, model, year)
        self.__battery_size = battery_size
        self.__engine = Engine(2)


    def set_battery_size(self, b_size):
        self.__battery_size = b_size

    def get_battery_size(self):
        return self.__battery_size

    def get_engine(self):
        return self.__engine


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


class Engine():

    def __init__(self, en_type):
        self._type = en_type  # 1 - двигатель внутреннего сгорания, 2 - электродвигатель
        if self._type == 1:
            self._fuel = 'бензин'
        else:
            self._fuel = 'электричество'

    def get_type(self):
        return self._type

    def get_fuel(self):
        return self._fuel

PAZ_32054 = Bus('Павловский автобусный завод', "ПАЗ-32054", 2023, 39)
Kamaz_65115 = Lorry('Камский автомобильный завод', "КамАЗ-65115", 2011)
my_wife_car = ElectricCar('Nissan', 'Leaf', 2015, 75)

print(f'Моя жена ездит на {my_wife_car.get_full_name()}. Этот автомобиль использует в качестве топлива '
      f'{my_wife_car.get_engine().get_fuel()}.')
print(f'Вчера я ехал на работу на автобусе {PAZ_32054._model}. Все {PAZ_32054.get_seats()} сиденья были заняты.')
print(f'На карьере работает {Kamaz_65115._model}, грузоподъемностью {Kamaz_65115.get_tonnage()} тонн. '
      f'Этот автомобиль использует в качестве топлива {Kamaz_65115.get_engine().get_fuel()}.')
