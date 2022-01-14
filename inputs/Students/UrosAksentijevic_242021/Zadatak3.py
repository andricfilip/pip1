n = int(input())
mat = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        mat[i][j] = int(input())

ans = [[0 for i in range(n)] for j in range(n)]
for i in range(0, n):
    for j in range(0, n):
        if(mat[i][j] == 1):
            for z in range(0, n):
                if(mat[j][z] == 1):
                    ans[i][z] = 1

for i in range(0, n):
    for j in range(0, n):
        if(mat[i][j] == 1):
            ans[i][j] = 1

for i in range(n):
    ans[i][i] = 1

for i in range(n):
    for j in range(n):
        print(ans[i][j], end = " ")
    print("")
