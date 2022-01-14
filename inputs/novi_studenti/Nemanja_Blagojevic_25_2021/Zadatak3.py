N=int(input())
mat=[]
for i in range (N):
    vrsta=[]
    for j in range(N):
        vrsta.append(int(input()))
    mat.append(vrsta)
N = 4
mat=[[0,1,0,1],[1,0,0,0],[1,1,0,0],[0,0,1,0]]
mat1=mat
for i in range(N):
    for j in range(N):
        if(i==j):
            mat1[i][j]==0
        elif (mat[i][j]==0):
            for p in range (N):
                if (mat[i][p]and(i !=p)):
                    if(mat[p][i]==1):
                        mat[i][j]=-1
                        break
                    
print(mat1)
