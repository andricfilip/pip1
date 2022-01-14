n=int(input())
mat=[[0 for i in range(n)]for j in range(n)]
mat1=[[0 for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        x=int(input())
        mat[i][j]=x
mat1=mat
for k in range(n):
    for c in range(n):
        for i in range(n):
            for j in range(n):
                if(mat1[k][c]==mat[i][j] or mat1[k][c]==1 or mat[i][j]==1):
                    mat1[k][c]=1
                else:
                   mat1[k][c]=0 
print(mat1)
