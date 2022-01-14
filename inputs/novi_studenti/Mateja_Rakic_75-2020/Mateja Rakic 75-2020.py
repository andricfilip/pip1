n=int(input())

matrica=[[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        matrica[i][j]=int(input())
        if(matrica[i][j]!=0 or matrica[i][j]!=1):
            print("unos nije dobar")


