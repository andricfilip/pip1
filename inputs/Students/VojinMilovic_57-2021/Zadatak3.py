def UcitajMatricu(n):
    mat = [[0 for i in range (n)] for i in range (n)]
    for i in range(n):
        for j in range(n):
            mat[i][j]=int(input())
    return mat
def StampajMatricu(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j], end="")
        print()

def main():
    n = int(input())
    mat = UcitajMatricu(n)
    mat1 = [[0 for i in range (n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if(i == j):
                mat[i][j] = 1
            if (mat[i][j] == 1):
                for k in range(n):
                    if(mat[j][k] == 1):
                        mat1[i][k]=1
                    if(mat[i][k] == 1):
                        mat1[j][k] = 1
    StampajMatricu(mat1)
main()