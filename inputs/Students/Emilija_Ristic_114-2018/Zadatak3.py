n = int(input())
mat = [[0 for i in range(n)]for j in range(n)]
for i in range(0,n):
    for j in range(0,n):
        mat[i][j] = int(input())
print(mat)
