n = int(input())
mat = [[0 for i in range (n)]for i in range (n)]
mat2 = [[0 for i in range (n)]for i in range(n)]
for i in range(n):
    for j in range(n):
        mat[i][j] = int(input())

i=0
j=-1
while(1):
    j += 1
    if(mat[i][j]==1):
        mat2[i][j]=1
        
    if(mat[i][j]!=1):
        for k in range(0,n):
            if(mat[i][k]==1):
                if(mat[k][j]==1):
                    mat2[i][j]=1
                    k=0
                    break
    if(i==j):
        mat2[i][j]=1

    if(i==n-1 and j==n-1):
        break
    if(j==n-1):
        i += 1
        j = -1

for i in range(0,n):
    print(mat2[i][:])
