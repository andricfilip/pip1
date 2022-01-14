N = int(input())
mat = []

for i in range(N):
    vrsta = []
    
    for j in range(N):
        vrsta.append(int(input()))

    mat.append(vrsta)

mat1 = mat

for i in range(N):
    for j in range(N):
        if(i==j): 
            mat1[i][j] = 1
        elif(mat[i][j] == 0):
            for k in range(N):
                if(mat[i][k] == 1) and (i!=k):
                    if(mat[k][j]==1):
                        mat1[i][j]=-1
                        break
                    
for i in range(N):
    linija=""
    
    for j in range(N):
        mat[i][j]=abs(mat[i][j])

        if(j==0):
            linija += str(mat[i][j])
        else:
             linija = "" + str(mat[i][j])
                
print(mat1)
                
    
