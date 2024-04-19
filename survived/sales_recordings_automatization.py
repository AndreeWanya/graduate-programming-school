def ShopOLAP(N: int, items: list) -> list:
    items = sorted(items)
    items_dict = {}
    for item in items:
        items_dict[item.split()[0]] = 0
    for item in items:
        items_dict[item.split()[0]] += int(item.split()[1])
    items = {}
    for value in items_dict.values():
        items[value] = []
    for key, value in items_dict.items():
        items[value].append(key)
    result = []
    for key in sorted(items, reverse=True):
        for value in sorted(items[key]):
            result.append(value + ' ' + str(key))

    return result


#print(ShopOLAP(5, ['платье1 5', 'сумка32 2', 'платье1 1', 'сумка23 2', 'сумка128 4']))
#print(ShopOLAP(8,['123 5','32 3','124 5','128 1','32 2','23 4','128 4','128 1']))
