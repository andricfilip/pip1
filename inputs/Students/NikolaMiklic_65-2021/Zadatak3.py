n = int(input())



for i in range(0,n):
    for j in range(0,n):
        mat[i][j] = 0

for i in range(0,n):
    for j in range(0,n):
        mat[i][j] = int(input())

for i in range(0,n):
    for j in range(0,n):
        mat2[i][j] = 0

for i in range(0,n):
    for j in range(0,n):
        if(i == j):
            mat2[i][j] = 1
        elif (mat[i][j] == 1):
            mat2[i][j] = 1
            for k in range(0,n):
                if(mat[j][k] == 1):
                    mat2[i][k] = 1
        else :
            print("Greska")
            
for i in range(0,n):
    for j in range(0,n):
        print(mat2[i][j])

