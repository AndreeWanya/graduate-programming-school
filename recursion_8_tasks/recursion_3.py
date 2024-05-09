def lists_length(lst: list) -> int:
    length = 1
    if len(lst) == 1:
        return length
    lst.pop(0)
    return length + lists_length(lst)


# lists = [[1, 2, 3, 4, 5], ['a', 'b', 'c', 'd'], [[0], [0], [0], [0], [0], [0]]]
# for lst in lists:
#     print(lists_length(lst))
