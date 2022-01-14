def direktan(mat,n):
    for i in range(n):
        for j in range(n):
            if(i==j):
                mat[i][j]=1
    
    for i in range(n):
        for j in range(n):
            if(mat[i][j]==0):

                if(i>j):
                    if(mat[i][j-1]==1 and mat[j-1][j]==1):
                        mat[i][j]=1
                
                if(i<j):
                    if(mat[i][j-1]==1 and mat[j-1][j]==1):
                        mat[i][j]=1

n=int(input())
mat=[[0 for i in range (n)] for j in range (n)]

for i in range(n):
    for j in range(n):
        mat[i][j]=int(input())

direktan(mat,n)
print(mat)
