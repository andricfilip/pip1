n=int(input("unesi n:"))
A=[[0 for i in range (n)]for i in range (n)]

for i in range (n):
    for j in range (n):
        A=int(input())
        A=A[i][j]


if (A[i]=A[j]):
    A[i][j]=1;
else:
    A[i][j]=0
if A[i][j]=A[i+1][j+1]:
    A[i][j]=1
else:
    a[i][j]=0;

if (A[i][j]=A[i][j+2]):
    A[i][j]=1
else:
    A[i][j]=0

NovMat=[[0 for i in range (n)]for i in range(n)]
for i in range (n):
    for j in range(n):
        NovMat= A[i][j]


print(NovMat)

