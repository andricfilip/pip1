
n=int(input())
A=[[0 for j in range(n)]for i in range(n)]
for i in range(n):
    for j in range(n):
        A[i][j]=int(input())
for i in range(n):
    for j in range(n):
        if(i==j):
            A[i][j]=1
        else:
            A[i][j]=0
for i in range(n):
    for j in range(n):
        print(A[i][j])

    
    
        
