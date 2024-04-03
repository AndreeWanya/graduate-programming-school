def squirrel(N: int) -> int:
    faq = 1
    for i in range(1, N+1):
        faq *= i
    return int(str(faq)[0])
