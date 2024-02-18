from my_package import module_1
from my_package.in_package import module_2
from my_package_2 import module_3

a = int(input('Введите a: '))
b = int(input('Введите b: '))

print('Сумма чисел:', module_1.sum(a, b))
print('Произведение чисел:', module_2.product(a, b))
print('Частное чисел:', module_2.division(a, b))
print('Частное суммы и произведения чисел:', module_3.my_def(a, b))
