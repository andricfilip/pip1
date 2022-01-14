n=int(input("Unesite broj gradova n: "))
A=[[0 for i in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        A[i][j]=int(input("Unesite 0 ili 1: "))



for i in range(n):
    for j in range(n):
         if(i==j):
             A[i][j]=1
         elif(A[i][j]==1):
             A[i][j]=1
         else:
             for r in range(n):
                 if(A[i][r]==1):
                     if(A[r][j]==1):
                         A[i][j]=1
                      
             
        
for i in range(n):
    print(A[i][:])
