N=int(input('n: '))
A=[[0 for i in range(N)] for i in range(N)]
mat=[[0 for i in range(N)] for i in range(N)]

for i in range(N):
    for j in range(N):
        x=int(input())
        A[i][j]=x
        
print(A)

for i in range(N):
    for j in range(N):
        for k in range(N):
            if (i==k):
                 mat[i][k]=1
            elif (A[i][k]==0):
                 continue
            else:
                 for p in range(N):
                     if(A[j][p]==1):
                         mat[i][k]=1
                     else:
                         continue

print(mat)
                        
