n=int(input())
mat=[[0 for j in range(n)]for i in range(n)]

for i in range(n):
    for j in range(n):
        mat[i][j]=int(input())


print(mat)



for i in range(n):
    for j in range(n):
        if(i==j):
            mat[i][j]=1


for i in range(n):            
    print(mat[i])

for i in range(n):
    for j in range(n):
        if(mat[i][j]==0):
            ind=j
            for i in range(n):
                if()
            
            
