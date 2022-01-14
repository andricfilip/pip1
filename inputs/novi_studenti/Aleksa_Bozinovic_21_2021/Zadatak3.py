N = int(input())
mat = []

for i in range(N):
    vrsta = []

    for j in range(N):    
        vrsta.append(int(input()))

    mat.append(vrsta)

mat1 = mat

for i in range(N):
    for j in range(N):
        if (i == j):
           mat1[i][j] = 1
        elif (mat[i][j] == 0):
            for p in range(N):
                if (mat[i][p] == 1) and (i != p):
                    if (mat[p][j] == 1):
                        mat[i][j] = -1
                        break

for i in range(N):
    line = ""
    
    for j in range(N):
        mat[i][j] = abs(mat[i][j])

        if (j == 0):
            line += str(mat[i][j])
        else:
            line += " " + str(mat[i][j])

    print(line)        
