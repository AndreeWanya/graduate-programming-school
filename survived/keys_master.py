def Keymaker(k: int) -> str:
    doors = ['1' for x in range(k)]
    for i in range(1, k):
        for j in range(i, k, i+1):
            if doors[j] == '0':
                doors[j] = '1'
            else:
                doors[j] = '0'
    return ''.join(doors)

# doors_quantity = [1, 2, 3, 4, 5, 10, 25, 100]
# for doors in doors_quantity:
#     print(Keymaker(doors))

