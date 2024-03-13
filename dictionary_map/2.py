from random import randint

def if_rep(my_list, n):
    rep_dict = {}
    for num in my_list:
        if num not in rep_dict and my_list.count(num) >= n:
            rep_dict[num] = my_list.count(num)
    return rep_dict

my_list = [randint(1, 10) for num in range(100)]
print(my_list)
N = int(input('Введите N: '))

result = if_rep(my_list, N)
print(list(result.keys()))



