n=int(input())
a=[[0 for i in range(n)]for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j]=int(input())
# 0 1 0 1   1 1 1 1 
# 1 0 0 0   1 1 0 1
# 1 1 0 0   1 1 1 1
# 0 0 1 0   1 1 1 1 
vrsta=[]
nije=[0]
for i in range(n):
    for j in range(n):
        k=1
        if a[i][j]==1 or a[i-1][j]==0 :
            vrsta.insert(j,1)
        else:
            vrsta.insert(j,0)                    
    
    print(vrsta)
    vrsta.clear()
