def UFO(N: int, data: list, octal: bool) -> list:
    result = []
    if octal:
        base = 8
    else:
        base = 16
    for d in data:
        result.append(int(str(d), base))
    return result

#print(UFO(2, [1234, 1777], False))
#print(UFO(2, [1234, 1777], True))