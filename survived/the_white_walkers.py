def white_walkers(village: str) -> bool:
    first = [0, 0]
    flag = False
    for i in range(len(village)):
        if village[i].isdigit() and int(first[0]) + int(village[i]) == 10:
            if village[first[1]: i].count('=') == 3:
                flag = True
                first = [village[i], i]
            else:
                return False
        elif village[i].isdigit():
            first = [village[i], i]
    return flag

# villages = ['axxb6===4xaf5===eee5', '5==ooooooo=5=5', 'abc=7==hdjs=3gg1=======5',
#             'aaS=8', '9===1===9===1===9']
# for village in villages:
#     print(white_walkers(village))