def UFO(N: int, data: list, octal: bool) -> list:
    result = []
    if octal:
        for d in data:
            result.append(int(str(d), 8))
    else:
        for d in data:
            result.append(int(str(d), 16))
    return result

#print(UFO(2, [1234, 1777], False))
#print(UFO(2, [1234, 1777], True))