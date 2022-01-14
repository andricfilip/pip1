n = int(input())
matrica = [[0 for i in range(n)] for j in range(n)]

nova_matrica = [[0 for i in range(n)] for j in range(n)]
for i in range(0,n):
    for j in range(0,n):
        t=int(input())
        matrica[i][j] = t

i = 0
j = 0
for i in range(i,n):
    for j in range(j,n+1):
        if(matrica[i][j] == 0):
            if(matrica[i][j+1] == 1):
                nova_matrica[i][j] = 0;
            else:
                if(matrica[i+1][j] == 1):
                    nova_matrica[i][j] = 1
                else:
                   nova_matrica[i][j] = 0
        else:
            nova_matrica[i][j] = 1
            


print(nova_matrica)

