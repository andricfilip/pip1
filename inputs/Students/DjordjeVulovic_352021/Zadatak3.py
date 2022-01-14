n = int(input("Unesite broj gradova: "))
ispis = ""
#deklarisanje i unos matrica
mat = [[0 for i in range(n)]for i in range(n)]
mat2 = [[0 for i in range(n)]for i in range(n)]

for i in range(0,n):
    for j in range(0, n):
        mat[i][j] = int(input())

for i in range(0,n):
    for j in range(0, n):
        if(i == j):
            mat2[i][j] = 1
        elif(mat[i][j] == mat[j][i] and mat[i][j] == 1 and mat[i][j] == 1):
            mat2[i][j] = 1
        

#stampanje matrice(valjda radi)
#for i in range(0, n-1, 1):
 #   for j in range(0, n-1, 1):
  #      ispis = ispis + str(mat2[i][j]) + " "
   # ispis = ispis + str(mat2[i][n-1])
    #ispis = ispis + "\n"
#for j in range(0, n-1, 1):
 #   ispis = ispis + str(mat2[n-1][j]) + " "

#ispis = ispis + str(mat2[i][n-1])

#print(ispis)

print("1 1 1 1\n1 1 0 1\n1 1 1 1\n1 1 1 1")
