
# Array of Edges (directed) [Start, End]
n = 8
A = [[0,1], [1,2], [0,3], [3,4], [3,6], [3,7], [4,2], [4,5], [5,2]]

print(A)

# Convert Array of Edges -> Adjancey Matrix
M = []

for i in range(n):
    M.append([0]*n)
    
for u, v in A:
    M[u][v] = 1
    

print(M)