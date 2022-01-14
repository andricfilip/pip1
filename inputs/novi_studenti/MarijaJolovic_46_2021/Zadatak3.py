n = int(input(""))

A = [[0 for i in range(n)] for j in range(n)]
B = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        A[i][j] = int(input(""))
#print(A)

for i in range(n):
    for j in range(n):
        if i==j:
            A[i][j]=1
#print(A)


for i in range(n):
    for j in range(n):
        if i==j:
            B[i][j]=1
        elif A[i][j]:
            B[i][j]=1
        elif A[i][j]==0:
            k=0
            while(k<n):
                if (k!=i and A[i][k] and A[k][j]):
                    #print(i,j,k)
                    B[i][j]=1
                    k=n
                else:
                    B[i][j]=0
                    k = k+1
for i in range(n):
    for j in range(n):
        print(B[i][j])
    print("\n")

