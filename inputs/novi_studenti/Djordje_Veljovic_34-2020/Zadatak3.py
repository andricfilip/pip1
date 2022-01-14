n=int(input())
A=[[0 for i in range (n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        A[i][j]=int(input())
B=[[0 for i in range (n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        if(i==j):
            B[i][j]=1
        
print(A)
print(B)
