def TransformTransform(A: list, N: int) -> bool:
    B = []
    for i in range(len(A) - 1):
        for j in range(len(A) - i - 1):
            k = i + j
            B.append(max(A[j: k + 1]))
    S = []
    for i in range(len(B) - 1):
        for j in range(len(B) - i - 1):
            k = i + j
            S.append(max(B[j: k + 1]))
    return sum(S) % 2 == 0

# print(TransformTransform([3, 2, 1], 3))
