from math import sqrt

def PatternUnlock(N: int, hits: list) -> str:
    unlock_code = 0
    for i in range(1, N):
        if abs(hits[i] - hits[i-1]) > 1:
            unlock_code += sqrt(2)
        else:
            unlock_code += 1
    unlock_code = str(unlock_code * 100000)
    unlock_code = unlock_code[:unlock_code.find('.')].strip('0')
    return unlock_code

#print(PatternUnlock(10, [1, 2, 3, 4, 5, 6, 2, 7, 8, 9]))