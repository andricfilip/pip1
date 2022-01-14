N=int(input())
A=[[0 for i in range(N)]for i in range (N)]

for i in range(N):
    for j in range(N):
        x=int(input())
        A[i][j]=x

NovaMat=[[0 for i in range(N)]for i in range (N)]

for i in range(N):
    for j in range(N):
        if(i==j):
            NovaMat[i][j]=1
        elif(A[i][j]==0):
            if(A[j][i]==1):
                NovaMat[i][j]=1
        elif( A[i][j]==1 ):
            NovaMat[i][j]=1

        else:
            NovaMat[i][j]=0
            for p in range (N):
                if(A[i][p]==1 and A[p][j]==1):
                        NovaMat[i][j]=1
                        break

print(NovaMat)
            
