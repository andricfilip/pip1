#  0 1 2 3
#0#0 1 0 1 ako su i j isti element=1, ako je element=0 trazi da li neko ij za
#1#1 0 0 0 isto i =1 i da li je ij za neko i isto j =1 osim i=j
#2#1 1 0 0
#3#0 0 1 0

n=int(input())

mat=[]
for i in range(n):
    vrsta=[]
    for j in range(n):
        vrsta.append(int(input()))
    mat.append(vrsta)
novmat=mat
pom1=False
pom2=False
p1=0                                           #21  23 3
for i in range(n):
    for j in range(n):
        if(mat[i][j]==0):
            for p in range(n):
                if(mat[i][p]==1):
                    pom1=10
                    p1=p
                if(mat[p1][j]==1):
                    pom2=10
            if(pom1+pom2==20):
                novmat[i][j]=1
        if(i==j):
            novmat[i][j]=1


vrsta=''
for i in range(n):
    for j in range(n):
        vrsta=vrsta+str(novmat[i][j])
    print(vrsta)
    vrsta=''


