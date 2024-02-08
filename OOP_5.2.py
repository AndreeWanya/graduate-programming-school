class Car():

    def __init__(self, color, autobody, max_speed):
        self._color = color
        self._body = autobody
        self._speed = max_speed

    def car_painting(self, new_color):
        self._color = new_color

class Daihatsu(Car):
    	
	def __init__(self, color, autobody, speed, model, year, gas_mileage, gas_tank_volume):
		super().__init__(color, autobody, speed)
		self.__model = model
		self.__year = year
		self.__gas_mileage = gas_mileage		# Расход бензина
		self.__gas_tank_vol = gas_tank_volume	# Объем бензобака
    		
	def get_model(self):
		return self.__model

	def get_distance(self):
		return (self.__gas_tank_vol / self.__gas_mileage) * 100

	def set_gas_volume(self, gas_vol):
		self.__gas_tank_vol = gas_vol

class Nissan(Car):

	def __init__(self, color, autobody, speed, model, year, electricity_consumption, battery_volume):
		super().__init__(color, autobody, speed)
		self.__model = model
		self.__year = year
		self.__el_consumption = electricity_consumption		# энергопотребление на 100 км
		self.__battery = battery_volume						# остаточная емкость батареи

	def get_model(self):
		return self.__model

	def get_battery(self):
		return self.__battery

	def get_distance(self):
		return (self.__battery / self.__el_consumption) * 100

	def charging_time(self, discharge, charger):
		return (self.__battery * discharge / 100) / charger

	def change_batery(self, new_battery):
		self.__battery = new_battery
    		
class Engine():
    		
	def __init__(self, type):
		self._type = type	# 1 - двигатель внутреннего сгорания, 2 - электродвигатель
		if type == 1:
			self._fuel = 'бензин'
		else:
			self._fuel = 'электричество'

	def get_type(self):
		return self._type
    			
class HC_E(Engine):
    		
	def __init__(self, type, volume, power, cylinder_num):
		super().__init__(type)
		self.__volume = volume
		self.__power = power
		self.__cylinder_num = cylinder_num

	def get_volume(self):
		return self.__volume

	def get_power(self):
		return self.__power

	def get_cylinder_num(self):
		return self.__cylinder_num

class EM61(Engine):

	def __init__(self, type, voltage, power):
		super().__init__(type)
		self.__voltage = voltage
		self.__power = power

	def get_voltage(self):
		return self.__voltage

	def get_power(self):
		return self.__power
    		
my_car = Daihatsu('белый', 'хэтчбек', 180, 'charade', 1999, 6, 45)
print(my_car.get_model())
print(my_car.get_distance())
my_car.set_gas_volume(40)
print(my_car.get_distance())

my_wife_car = Nissan('черный', 'хэтчбек', 144, 'leaf', 2015, 15, 30)
print(my_wife_car.get_battery())
print('На зарядку вашего автомобиля потребуется', my_wife_car.charging_time(30, 6.6), 'часов')
my_wife_car.change_batery(24)
print(my_wife_car.get_battery())

my_car.car_painting('синий')
print(my_car._color)

my_car_engine = HC_E(1, 1295, 91, 4)
my_wife_car_engine = EM61(2, 380, 109)

print('Мой автомобиль', my_car.get_model(), 'имеет двигатель внутреннего сгорания объемом', my_car_engine.get_volume(), 'куб см и мощностью', my_car_engine.get_power(), 'лошадинных сил.')
print('Автомобиль моей жены', my_wife_car.get_model(), 'имеет электродвигатель мощностью', my_wife_car_engine.get_power(), 'лошадинных сил.')

    	
