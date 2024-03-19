class Engine():
    """ Любой двигатель имеет мощность в лошадинных силах и ваттах"""

    def __init__(self, horsepower, wattage):
        self._wattage = wattage
        self._horsepower = horsepower

    def set_wattage(self, wat):
        self._wattage = wat

    def set_horsepower(self, hp):
        self._horsepower = hp

    def get_power(self):
        power = f"Мощность двигателя составляет {self._horsepower}Лс/{self._wattage}Ватт"
        return power


class ElectricEngine(Engine):
    """ Двигатель электромобиля """

    def __init__(self, horsepower, wattage):
        super().__init__(horsepower, wattage)
        self.__voltage = 380
        self.__fuel = 'электричество'

    def set_voltage(self, volt):
        self.__voltage = volt

    def get_voltage(self):
        return self.__voltage

    def get_fuel(self):
        return self.__fuel


class GasEngine(Engine):
    """ Двигатель внутреннего сгорания """

    def __init__(self, horsepower, wattage, volume_eng):
        super().__init__(horsepower, wattage)
        self.__volume_emg = volume_eng
        self.__fuel = '92 бензин'

    def set_fuel(self, fuel_mark):
        self.__fuel = fuel_mark

    def get_fuel(self):
        return self.__fuel

    def get_volume_eng(self):
        return self.__volume_emg


class Car():
    """ Любой автомобиль """

    def __init__(self, maker, model, year):
        self._maker = maker
        self._model = model
        self._year = year
        self._engine = Engine(0, 0)

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
        self.__engine = ElectricEngine(0, 0)

    def set_battery_size(self, b_size):
        self.__battery_size = b_size

    def get_battery_size(self):
        return self.__battery_size

    def get_engine(self):
        return self.__engine

    def set_engine(self, engine: ElectricEngine):
        self.__engine = engine


class Lorry(Car):
    """ Грузовик """

    def __init__(self, maker, model, year):
        super().__init__(maker, model, year)
        self.__tonnage = 15
        self.__engine = GasEngine(0, 0, 0)

    def set_tonnage(self, ton):
        self.__tonnage = ton

    def get_tonnage(self):
        return self.__tonnage

    def get_engine(self):
        return self.__engine

    def set_engine(self, engine: GasEngine):
        self.__engine = engine


class Bus(Car):
    """ Автобус """

    def __init__(self, maker, model, year, seats):
        super().__init__(maker, model, year)
        self.__seats = seats

    def get_seats(self):
        return self.__seats

    def set_seats(self, pass_seats):
        self.__seats = pass_seats


class Engine():
    """ Любой двигатель имеет мощность в лошадинных силах и ваттах"""

    def __init__(self, horsepower, wattage):
        self._wattage = wattage
        self._horsepower = horsepower

    def set_wattage(self, wat):
        self._wattage = wat

    def set_horsepower(self, hp):
        self._horsepower = hp

    def get_power(self):
        power = f"Мощность двигателя составляет {self._horsepower}Лс/{self._wattage}Ватт"
        return power


class ElectricEngine(Engine):
    """ Двигатель электромобиля """

    def __init__(self, horsepower, wattage):
        super().__init__(horsepower, wattage)
        self.__voltage = 380
        self.__fuel = 'электричество'

    def set_voltage(self, volt):
        self.__voltage = volt

    def get_voltage(self):
        return self.__voltage

    def get_fuel(self):
        return self.__fuel


class GasEngine(Engine):
    """ Двигатель внутреннего сгорания """

    def __init__(self, horsepower, wattage, volume_eng):
        super().__init__(horsepower, wattage)
        self.__volume_emg = volume_eng
        self.__fuel = '92 бензин'

    def set_fuel(self, fuel_mark):
        self.__fuel = fuel_mark

    def get_fuel(self):
        return self.__fuel

    def get_volume_eng(self):
        return self.__volume_emg


PAZ_32054 = Bus('Павловский автобусный завод', "ПАЗ-32054", 2023, 39)
Kamaz_65115 = Lorry('Камский автомобильный завод', "КамАЗ-65115", 2011)
my_wife_car = ElectricCar('Nissan', 'Leaf', 2015, 75)

print(f'Моя жена ездит на {my_wife_car.get_full_name()}. Этот автомобиль использует в качестве топлива '
      f'{my_wife_car.get_engine().get_fuel()}.')
print(f'Вчера я ехал на работу на автобусе {PAZ_32054._model}. Все {PAZ_32054.get_seats()} сиденья были заняты.')
print(f'На карьере работает {Kamaz_65115._model}, грузоподъемностью {Kamaz_65115.get_tonnage()} тонн. '
      f'Этот автомобиль использует в качестве топлива {Kamaz_65115.get_engine().get_fuel()}.')
