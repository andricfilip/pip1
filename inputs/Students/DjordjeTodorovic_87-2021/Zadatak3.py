#ako ne moze i,j onda gledamo i sve ostalo sto je 1
#ako to ostalo ima 1 u j onda stavljamo 1
n=int(input())
s=""
a=[[0 for i in range(n)]for i in range(n)]
fin=[[0 for i in range(n)]for i in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j]=int(input())

for i in range(n):
    for j in range(n):
        if (i==j):
            fin[i][j]=1;
        elif (a[i][j]==1):
            fin[i][j]=1
        else:
            for k in range(n):
                if (a[i][k]==1):
                    if (a[k][j]==1):
                        fin[i][j]=1;
#stampa matricu (ne znam laksi nacin)
for i in range(0,n-1,1):
    for j in range(0,n-1,1):
        s+=str(fin[i][j])+" "
    s+=str(fin[i][n-1])
    s+="\n"
for j in range(0,n-1,1):
    s+=str(fin[n-1][j])+" "
s+=str(fin[i][n-1])
print(s);
