matrix=[]
n=int(input())
for i in range(n):
    a=[]
    for j in range(n):
        a.append(int(input()))
    matrix.append(a)
for i in range(n):
    for j in range(n):
        if(matrix[i][j]!=1):
            if(i==j):
                matrix[i][j]=1
            else:
                for k in range(n):
                    for c in range(n):
                        if(k!=i and c!=j and k==j and c==i):
                            if(matrix[k][c]==1):
                                matrix[i][j]=1
for i in range(n):
    for j in range(n):
        if(matrix[i][j]==2):
            matrix[i][j]=matrix[i][j]-1
        print(matrix[i][j],end='  ')
    print()
                
