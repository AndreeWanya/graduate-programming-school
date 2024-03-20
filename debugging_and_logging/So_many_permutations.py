import logging

def permutations(s):
    assert isinstance(s, str)
    result = []
    logging.debug(f'На вход функции permutation() получено: {s}.')
    if len(s) == 1:
        return list(s)
    if len(s) == 2:
        return list(set([s[0] + s[1], s[1] + s[0]]))
    else:
        # assert len(s) != 0
        for i in range(len(s)):
            s1 = s[:i] + (s[i+1:])
            logging.info(f'на вход получено {s1}.')
            for permut in permutations(s1):
                c = s[i] + permut
                result.append(c)
        return(list(set(result)))

logging.basicConfig(level=logging.INFO, filename='my_log.log', filemode='w', format='%(asctime)s %(levelname)s %(funcName)s %(message)s')
print(permutations('a'))
print(permutations('ab'))
print(permutations('abc'))
print(permutations('aabb'))
print(permutations(''))
print(permutations(12345))
