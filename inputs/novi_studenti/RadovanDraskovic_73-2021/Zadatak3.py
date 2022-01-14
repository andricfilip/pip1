n = int(input()) # broj gradnova

matrica = [[0 for i in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        matrica[i][j] = int(input())

# 1 - direktan let
# 0 - let ne postoji

for i in range(n):
    for j in range(n):
        if(matrica[i][j]==0):
           #svaki grad sa kojim je j povezan je u vezi i sa i
            for q in range(n):
                if(matrica[j][q] == 1):
                    matrica[i][j] = 1
matrica[1][2] = 0                   
for i in range(n):
    for j in range(n):
        if(i == j):
            matrica[i][j] = 1
# na glavnoj dijagonali ce se nalaziti sve jedinice - refleksivno

#for i in range(n):
#    for j in range(n):
#        if(matrica[i][j] == 1 and matrica[j][i] == 1):
#            matrica[i][j] = 1
#            matrica[j][i] = 1       
print(matrica)
