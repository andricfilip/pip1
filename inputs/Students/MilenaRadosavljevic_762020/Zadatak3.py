n=int(input())
mat=[[0 for i in range(n)]for j in range(n)]

for i in range(n):
    for j in range(n):
        mat[i][j]=int(input())

mat1=[[0 for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        if(i==j or mat[i][j]==1):
            mat1[i][j]=1
        else:
            if(mat[j][i]==1):
                mat1[i][j]=1
            else:
                mat1[i][j]=0
    #print(mat1[i])
        
for i in range(n):
    print(mat1[i])
