def BiggerGreater(input_s: str) -> str:
    if input_s[0] * len(input_s) == input_s:
        return ''
    new_s = input_s
    s_list = []
    for j in range(100):
        for i in range(1, len(input_s)):
            new_s = new_s[:-i-1] + new_s[-i] + new_s[-i-1] + new_s[:-i:-1][::-1]
            s_list.append(new_s)
        if input_s in s_list:
            break

    s_list = [x for x in s_list if x > input_s]
    if len(s_list) == 0:
    	return ''
    else:
    	return min(s_list)

#str_list = ['ая', 'fff', 'нклм', 'вибк', 'вкиб', 'b', 'za']
#for s in str_list:
#    print(BiggerGreater(s))