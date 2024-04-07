from math import sqrt

def PatternUnlock(N: int, hits: list) -> str:
    unlock_code = 0
    points = ['654', '123', '987']
    for i in range(1, N):
        if str(hits[i]) in points[0] and str(hits[i-1]) in points[1] and points[0].find(str(hits[i])) != points[1].find(str(hits[i-1])):
            unlock_code += sqrt(2)
        elif str(hits[i]) in points[1] and str(hits[i-1]) in points[2] and points[1].find(str(hits[i])) != points[2].find(str(hits[i-1])):
            unlock_code += sqrt(2)
        elif str(hits[i]) in points[2] and str(hits[i-1]) in points[1] and points[2].find(str(hits[i])) != points[1].find(str(hits[i-1])):
            unlock_code += sqrt(2)
        elif str(hits[i]) in points[1] and str(hits[i-1]) in points[0] and points[1].find(str(hits[i])) != points[0].find(str(hits[i-1])):
            unlock_code += sqrt(2)
        else:
            unlock_code += 1
    unlock_code = str(round(unlock_code * 100000))
    print(unlock_code)
    return unlock_code.strip('0')

#print(PatternUnlock(10, [1, 2, 3, 4, 5, 6, 2, 7, 8, 9]))
#print(PatternUnlock(3, [2, 1, 9]))
