def one_transform(A: list) -> list:
    B = []
    for i in range(len(A)):
        for j in range(len(A) - i):
            k = i + j
            B.append(max(A[j: k + 1]))
    return B

def TransformTransform(A: list, N: int) -> bool:
    S = one_transform(one_transform(A))
    # print(sum(S))
    return sum(S) % 2 == 0

# print(TransformTransform([3, 2, 1], 3))
# print(TransformTransform([1,2,1,7,2,4,3,1,5,1,2,1,6,1,2], 15))