n=int(input())
matrix=[[0 for i in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][j]=int(input())

for i in range(n):
    for j in range(n):
        if(j==n-1):
            break
        if(i==j):
            matrix[i][j]=1
        else:
            if(matrix[i][j]==1 and matrix[i][j+1]==0 ):
                if(matrix[j][j+1]==1 or matrix[j+1][j]==1):
                    matrix[i][j]=1
            else:
                matrix[i][j]=0
        
for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=' ')
    print()

