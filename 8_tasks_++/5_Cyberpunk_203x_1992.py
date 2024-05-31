def massdriver(activate: list) -> int:
    my_dict = {}
    result = -1
    for i in range(len(activate)):
        if activate[i] not in my_dict:
            my_dict[activate[i]] = i
        elif my_dict[activate[i]] < result or result == -1:
            result = my_dict[activate[i]]
    return result

# arrs = [[1, 2, 3, 1, 2, 3, 4], [1, 2, 3, 4, 3, 4, 2], [1, 2, 3, 4, 5, 6, 7]]
# for arr in arrs:
#     print(massdriver(arr))
