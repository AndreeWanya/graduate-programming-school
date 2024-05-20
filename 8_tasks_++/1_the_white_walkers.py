def white_walkers(village: str) -> bool:
    first_digit = 0
    walkers = 0
    flag = False
    for c in village:
        if c.isdigit():
            if int(c) + first_digit == 10 and walkers == 3:
                flag = True
            elif int(c) + first_digit == 10 and walkers != 3:
                return False
            first_digit = int(c)
            walkers = 0
        elif c == '=':
            walkers += 1
    return flag


# villages = ['axxb6===4xaf5===eee5', '5==ooooooo=5=5', 'abc=7==hdjs=3gg1=======5',
#             'aaS=8', '9===1===9===1===9']
# for village in villages:
#     print(white_walkers(village))
