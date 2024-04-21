def BastShoe(command: str) -> str:
    if command[0] == '1':
        return commands_history[-1] + command[2:]
    elif command[0] == '2':
        if int(command[2:]) > len(commands_history[-1]):
            return ''
        else:
            return commands_history[-1][:-2]
    elif command[0] == '3':
        if int(command[2:]) > len(commands_history[-1]):
            return ''
        else:
            return commands_history[-1][int(command[2:])]
    elif command[0] == '4':
        pass
    elif command[0] == '5':
        pass
    else:
        return actual_line

commands = ['1 Привет', '1 , Мир!', '1 ++', '2 2', '4', '4', '1 *', '4', '4', '4', '3 6', '2 100',
            '1 Привет', '1 , Мир!', '1 ++', '4', '4', '5', '4', '5', '5', '5', '5', '4', '4', '2 2',
            '4', '5', '5', '5']

commands_history = ['']
actual_line = ''
for command in commands:
    print(BastShoe(command))