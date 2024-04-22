def BastShoe(command: str) -> str:
    global actual_line, lines_history
    if command[0] == '1':
        actual_line += command[2:]
        lines_history.append(actual_line)
    elif command[0] == '2':
        if int(command[2:]) > len(actual_line):
            actual_line = ''
        else:
            actual_line = actual_line[:-int(command[2:])]
            #print(lines_history)
        lines_history.append(actual_line)
    elif command[0] == '3':
        if int(command[2:]) > len(actual_line):
            return ''
        else:
            return actual_line[int(command[2:])]
    elif command[0] == '4':
        #print(lines_history)
        if len(lines_history) >= 1:
        	actual_line = lines_history[-2]
        	lines_history.append(actual_line)
    elif command[0] == '5':
        pass
    return actual_line

commands = ['1 Привет', '1 , Мир!', '1 ++', '2 2', '4', '4', '1 *', '4', '4', '4', '3 6', '2 100',
            '1 Привет', '1 , Мир!', '1 ++', '4', '4', '5', '4', '5', '5', '5', '5', '4', '4', '2 2',
            '4', '5', '5', '5']

lines_history = []
actual_line = ''
for command in commands:
    print(BastShoe(command))