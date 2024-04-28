def MatrixTurn(Matrix: list, M: int, N: int, T: int):
    if M > N:
        main_size = N
    else:
        main_size = M
    for t in range(T):
        Matrix_1 = Matrix.copy()
        mtrx = [list(x) for x in Matrix_1]
        for i in range(int(main_size / 2)):
            num = Matrix_1[1][0]
            for j in range(len(Matrix_1[0])):
                mtrx[i][i + j], num = num, Matrix_1[0][j]
            for j in range(len(Matrix_1) - 2):
                mtrx[i + j + 1][-i - 1], num = num, Matrix_1[j + 1][-1]
            for j in range(len(Matrix_1[0])):
                mtrx[-i - 1][-i - j - 1], num = num, Matrix_1[-1][-j - 1]
            for j in range(len(Matrix_1) - 2):
                mtrx[-i - j - 2][i], num = num, Matrix_1[-j - 2][0]
            Matrix_1 = [x[1:-1] for x in Matrix_1[1:-1]]
        Matrix.clear()
        for m in mtrx:
            Matrix.append(''.join(m))

#Matrix = ['123456', '234567', '345678', '456789']
#MatrixTurn(Matrix, 4, 6, 1)
# MatrixTurn(['123456', '234567', '345678', '456789', '567890', '678901'], 6, 6, 3)
# MatrixTurn(['123456', '234567', '345678', '456789', '567890', '678901', '456789', '987654'], 8, 6, 3)
# MatrixTurn(['12345', '23456', '34567', '45678', '56789', '67890'], 6, 5, 3)
#print(Matrix)