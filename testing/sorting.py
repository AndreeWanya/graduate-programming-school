import random

def create_list(n, m):
    my_list = []
    for i in range(n):
        my_list.append(random.randint(1, 100))
    return my_list

def sorting_list(my_list, n, m):
    for i in range(n):
        for j in range(m):
            if my_list[j] > my_list[m - 1]:
                my_list[m - 1], my_list[j] = my_list[j], my_list[m - 1]
        m -= 1
    return my_list

n = 10
m = n

result = create_list(n, m)
print(result)
print(sorting_list(result, n, m))
