def uVezi(j, k):
    if j == k:
        return 1
    if a[j][k] == 1:
        return 1

    for i in range(n):
       if(a[j][i]==1):
           if(a[i][k]==1):
               return 1
            
    return 0

n = int(input())
a = [[0 for i in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j] = int(input())

b = [[0 for i in range(n)] for i in range(n)]

for x in range(n):
    for y in range(n):
        b[x][y] = uVezi(x,y)


for y in range(n):
    broj = 0
    for x in range(n):
        broj += b[x][n-y-1]*(10**x)
    brojstr = str(broj)
    while(len(brojstr)<n):
        brojstr = "0"+brojstr
    print(brojstr)
        
