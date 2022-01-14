n=int(input("gradovi "))

a=[[0 for i in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        
        a[i][j]=int(input("direktnost je "))
        if i==j:
            a[i][j]=1


print(a)

i=0
j=0

x=[[0 for i in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            x[i][j]=a[i][j]
        else:
            for p in range(n):
                s=0
                if a[i][p]==1:
                    
                    if a[p][j]==1:
                        s=1
                        x[i][j]=1
                        break
                        



print(x)
