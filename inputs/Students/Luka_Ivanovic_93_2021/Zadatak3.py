N=int(input())
a=[]
mat=[[0 for i in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        x=int(input())
        mat[i][j]=x

mat2=[[0 for i in range(N)] for i in range(N)]

for i in range(N):
    for j in range(N):
        if(i==j):
            mat2[i][j]=1
        elif(mat[i][j]==1):
            mat2[i][j]=1
            mat2[j][i]=1

for i in range(N):
    for j in range(N):
        a=a+[mat2[i][j]]
    print(a)
    a=[]
    
