n=int(input("Unesite broj gradova:"))

mat=[[0 for j in range(n)]for i in range(n)]

for i in range(n):
    for j in range(n):
        print("Unesite element")
        mat[i][j]=int(input())

print(mat)

for i in range(n):
    for j in range(n):
        if((i==j)):
            mat[i][j]=1
        elif((i!=j)and (i>j)): 
           mat[i][j]=1


print(mat)

