n=int(input())
mat=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        mat[i][j]=int(input())

nova=[[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        nova[i][j]=mat[i][j]
            
for i in range(n):
    for j in range(n):
        if(i==j):
            nova[i][j]=1
        if(mat[i][j]==0):
            a=i
            b=j
            for c in range(0,n):
                if(i!=c):
                    if(mat[i][c]==1):
                        if(mat[c][j]==1):
                            nova[i][j]=1
                         
                            
                 
                            
print(nova)
