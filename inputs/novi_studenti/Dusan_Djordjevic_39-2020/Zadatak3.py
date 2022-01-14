n=int(input())
mat=[]
mat1=mat
for i in range(n):
    vrsta=[]
    for j in range(n):
        vrsta.append(int(input()))
    mat.append(vrsta)
for i in range(n):
    for j in range(n):
        if(i==j):
for i in range(n):
    for j in range(n-1):
        if(mat[i][j]==0):
            if(mat[i][j+1]==0):
                mat[i][j]=0
    for j in range(n-1):
        for k in range(j+1,n):
            if(mat[i][j]==0):
                if(mat[i][k]==1):
                    
for i in range(n):
    for j in range(n):
        print(mat1[i][j], end=" ")
    print()
