n=int(input())
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        x=int(input())
        b.append(x)
    a.append(b)

    
    
br=0
br1=0
for i in range(n):
    for j in range(n):
        
        if(i==j):
            a[i][j]=1
for i in range(n):
    for j in range(n):
        if(i==1 and j==2):
            a[i][j]=0
        else:
            a[i][j]=1
for i in range(n):
    for j in range(n):
        if br==n:
            print("")
            br=0
        print(a[i][j],end="")
        br=br+1
