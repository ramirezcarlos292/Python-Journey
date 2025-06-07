M = [[1, 2], [3, 4]]
N = [[1, 2], [3, 4]]

length = len(M)
for i in range(length):
    for j in range(length):
        print(M[i][j]*N[j][i])
        

