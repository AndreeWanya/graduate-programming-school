def digital_rain(col: str) -> str:
    print(col)
    the_long_line, s_1, s_2 = '', '', ''
    step_1, step_2 = 1, 1
    for i in range(len(col) // 2, len(col)):
        if col[i] != col[i - step_1]:
            s_1 = col[i - step_1] + s_1 + col[i]
            # print('s_1', s_1, i, step_1)
            step_1 += 2
        # elif col[i - 1] != col[i - 1 - step_1]:
        #     s_1 = col[i - 1 - step_1] + s_1[:-1] + col[i - 1]
        #     step_1 += 2
        else:
            s_1 = ''
            step_1 = 1
        # print(col[-i], col[-i + step_2], step_2, i)
        if col[-i + 1] != col[-i + 1 + step_2]:
            s_2 = col[-i + 1] + s_2 + col[-i + 1 + step_2]
            # print('s_2', s_2, i, step_2)
            step_2 += 2
        else:
            if col[-i + 1] != col[-i + 1 + step_2 - 2] and len(s_2) != 0:
                s_2 = col[-i + 1] + s_2[: -1]
            else:
                s_2 = ''
                step_2 = 1

        if len(s_1) > len(the_long_line):
            the_long_line = s_1
        if len(s_2) >= len(the_long_line):
            the_long_line = s_2
    return the_long_line

strings = ['1111000', '11101000', '011111110', '11111111']
# strings = ['1010101000000']
for s in strings:
    print('1', digital_rain(''.join(reversed(s))))
    print('2', digital_rain(s))