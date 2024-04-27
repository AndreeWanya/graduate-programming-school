def MatrixTurn(Matrix: list, M: int, N: int, T: int) -> None:
    mtrx_of_strs = []
    for i in range(int(M/2)):
    	mtrx_to_str = Matrix[i][i:N-i]
    	if i+1 == M/2:
    		mtrx_to_str += ''.join(reversed(Matrix[-i-1][i:N-i]))
    		mtrx_of_strs.append(mtrx_to_str)
    		continue
    	for j in range(M-2):
    		mtrx_to_str += Matrix[j+1][-i-1]
    	mtrx_to_str += ''.join(reversed(Matrix[-i-1][i:N-i]))
    	for j in range(M-2):
    		mtrx_to_str += Matrix[-j-2][i]
    	mtrx_of_strs.append(mtrx_to_str)
    
    for i in range(len(mtrx_of_strs)):
    	mtrx_of_strs[i] = mtrx_of_strs[i][-1] + mtrx_of_strs[i][:-1]
    	Matrix[i] = Matrix[i][:i+1] + mtrx_of_strs[i][:N-i] + Matrix[i][N-i:]
    	if i+1 == len(mtrx_of_strs):
    		Matrix[-i-1] = Matrix[-i-1][i] + ''.join(reversed(mtrx_of_strs[i][N-i:-N-i-1]))
    		print(Matrix)
    		continue
    	for j in range(len(mtrx_of_strs)):
    		Matrix[j+1] = Matrix[j+1][:-i-1] + mtrx_of_strs[i][N+ j]
    		print(Matrix)
    	print()
    	print(mtrx_of_strs[i])
    	Matrix[-i-1] = ''.join(reversed(mtrx_of_strs[i][N + len(mtrx_of_strs):N + len(mtrx_of_strs) + N]))
    	for j in range(len(mtrx_of_strs)):
    		Matrix[j+1] = Matrix[j+1][:i] + mtrx_of_strs[i][N + len(mtrx_of_strs) + j] + Matrix[j+1][i+1:]
    print(Matrix)
    	
      	   	
MatrixTurn(['123456', '234567', '345678', '456789'], 4, 6, 3)