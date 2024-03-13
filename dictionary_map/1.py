import random

keys_list = [key for key in range (1, 101)]
my_dict = dict()
for key in keys_list:
    my_dict[key] = str(random.randint(100, 1000))

for i in range(1, 101):
    print(my_dict.pop(i))

print(my_dict)
