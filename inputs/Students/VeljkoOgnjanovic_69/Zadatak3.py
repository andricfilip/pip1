#Zadatak 3
n = int(input("Unesite dimenzije matrice n = "))
a = []

a = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        x = input("a[%d][%d] = "%(i,j))
        a[i][j] = x

#posto je svaki u relaviji sa samim sobom
for i in range(n):
    for j in range(n):
        if(i == j):
            a[i][j] = 1

#ne znam sto ovo nece 
for i in range(n):
    for j in range(n):
        k = j - 1
        if(a[i][j] == 1) and (a[j][k] == 1):
            a[i][k] = 1

#ispis matrice
for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")
    print("")
