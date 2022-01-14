n=int(input())
matrica=[[0 for i in range(n)] for j in range(n)]
novamatrica=[[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        matrica[i][j]=int(input())

for i in range(n):
    for j in range(n):
        if(matrica[i][j]==1):
            novamatrica[i][j]==1
        else:
            novamatrica[i][j]=0
for i in range(n):
    novamatrica[i][i]==1
    
print(novamatrica)
                    
