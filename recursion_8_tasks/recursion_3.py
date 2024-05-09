def lists_length(lst: list) -> int:
    if len(lst) == 1:
        return 1
    lst.pop(0)
    return 1 + lists_length(lst)


# lists = [[1, 2, 3, 4, 5], ['a', 'b', 'c', 'd'], [[0], [0], [0], [0], [0], [0]]]
# for lst in lists:
#     print(lists_length(lst))
