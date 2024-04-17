def LineAnalysis(line: str) -> bool:
    if '.' not in line:
        return True
    #elif line[0] != '*' or line[-1] != '*':
    #    return False
    sub_line = line[0: line.find('*', line.find('.'))]
    for i in range(len(sub_line), len(line), len(sub_line)):
        if line[i-len(sub_line): i] != sub_line:
            return False
    if line[i:] == '*' * len(line[i:]):
        return True
    return False

#print(LineAnalysis('*..*..*..*..*..*..*'))
#print(LineAnalysis('*..*...*..*..*..*..*'))
#print(LineAnalysis('*..*..*..*..*..**..*'))
#print(LineAnalysis('*'))
#print(LineAnalysis('***'))
#print(LineAnalysis('*.......*.......*'))
#print(LineAnalysis('**'))
#print(LineAnalysis('*.*'))