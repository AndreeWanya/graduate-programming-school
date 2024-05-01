def Football(F: list, N: int) -> bool:
    if list(reversed(F)) == sorted(F):
        return True
    if F == sorted(F):
        return False
    for i in range(N-1):
        for j in range(i+1, N):
            if F[:i] + [F[j]] + F[i+1:j] + [F[i]] + F[j+1:] == sorted(F):
                return True
            elif F[:i] + list(reversed(F[i:j])) + F[j:] == sorted(F):
                return True
    return False

# examples = [[1, 3, 2], [3, 2, 1], [1, 7, 5, 3, 9], [9, 5, 3, 7, 1], [1, 4, 3, 2, 5], [1, 2, 3]]
# for example in examples:
#     print(Football(example, len(example)))