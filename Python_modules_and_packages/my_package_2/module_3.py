from my_package import module_1
from my_package.in_package import module_2

def my_def(a, b):
    return module_2.division(module_1.sum(a, b), module_2.product(a, b))
