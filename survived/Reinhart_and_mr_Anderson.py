def BigMinus(s1: str, s2: str) -> str:
    if len(s2) > len(s1):
        s1, s2 = s2, s1
    elif int(s2[0]) > int(s1[0]):
        s1, s2 = s2, s1
    s2 = (len(s1) - len(s2)) * '0' + s2
    av_value = ''
    n = 0
    for i in range(1, len(s1)+1):
        n = int(s1[-i]) - int(s2[-i]) - n
        if n >= 0:
            av_value = str(n) + av_value
            n = 0
        else:
            av_value = str(10 + n) + av_value
            n = 1
    return av_value

#print(BigMinus('1234567891', '1'))
#print(BigMinus('1', '321'))
#print(BigMinus('123456789', '987654321'))
