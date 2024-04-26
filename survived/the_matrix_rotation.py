def string_to_matrix(external_circle: str, m: int, n: int) -> list:
	matrix = [external_circle[:n]]
	if m == 2:
		return matrix += [external_circle[-1: -1-n]]
	for i in range(len(m/2)):
		matrix.append(external_circle)
		

def circle_to_string(Matrix: list, M: int, N: int, i: int) -> str:
	external_circle = Matrix[i][i:N-i]
	if i+1 == M/2:
	   external_circle += ''.join(reversed(Matrix[-i-1][i:N-i]))
	   continue
    for j in range(M-2):
    	external_circle += Matrix[j+1][-i-1]
    external_circle += ''.join(reversed(Matrix[-i-1][i:N-i]))
    for j in range(M-2):
    	external_circle += Matrix[-j-2][i] 	
    return external_circle
    
def MatrixTurn(Matrix: list, M: int, N: int, T: int) -> None:
    for i in range(int(M/2)):
    	external_circle = circle_to_string(Matrix, M, N, i)
    	external_circle = external_circle[-1] + external_circle[0:-1]
    	   	
MatrixTurn(['123456', '234567', '345678', '456789'], 4, 6, 3)