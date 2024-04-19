def ShopOLAP(N: int, items: list) -> list:
    items = sorted(items)
    del_items = []
    for i in range(N-1):
    	if items[i].split()[0] == items[i+1].split()[0]:
    		items[i] = items[i].split()[0] + ' ' + str(int(items[i].split()[1]) + int(items[i+1].split()[1]))
    		del_items.append(i+1)
    for item in del_items:
    	del items[item]
    sorted_items = {}
    for item in items:
    	sorted_items[int(item.split()[1])] = []
    for item in items:
    	sorted_items[int(item.split()[1])].append(item.split()[0])
    print(sorted_items)
    return items

print(ShopOLAP(5, ['платье1 5', 'сумка32 2', 'платье1 1', 'сумка23 2', 'сумка128 4']))