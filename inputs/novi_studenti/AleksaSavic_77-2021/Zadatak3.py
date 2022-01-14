n = int(input())

mat =  []
mat2 = []

for i in range (n):
    a = []
    for j in range (n):
        a.append(int(input()))
    mat.append(a)
    mat2.append(a)

for i in range (n):
    mat2[i][i] = 1

for i in range (n):
    for j in range (n):
        if (mat[i][j] == 0):
            for k in range (n):
                if (mat[i][k] == 1 and mat[k][j] == 1):
                    mat2[i][j] = 1
                    break;


for i in range (n):
    for j in range (n):
        print(mat2[i][j])

