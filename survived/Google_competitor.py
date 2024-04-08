def WordSearch(len_sub: int, s: str, subs: str) -> list:
    if len(s) < len_sub:
        if subs in s:
            return [1]
    new_line = ''
    subs_list = []
    for i in range(len(s)):
        new_line += s[i]
        if len(new_line) == len_sub and s[i] == ' ':
            subs_list.append(new_line)
            new_line = ''
        elif len(new_line) == len_sub and s[i] != ' ':
            if ' ' in new_line[::-1]:
                subs_list.append(new_line[:-new_line[::-1].find(' ')-1])
                new_line = new_line[-new_line[::-1].find(' '):]
            else:
                subs_list.append(new_line[:len_sub-1] + '-')
                new_line = new_line[len_sub:]
    result_list = []
    for sub in subs_list:
        if subs in sub.split(' '):
            result_list.append(1)
        else:
            result_list.append(0)
    return result_list

#print(WordSearch(12, '1) cnhjrf hfp,bdftncz yf yf,jh cnhjr xthtp dshfdybdfybt gj pflfyyjq ibhbyt/', 'cnhjr'))