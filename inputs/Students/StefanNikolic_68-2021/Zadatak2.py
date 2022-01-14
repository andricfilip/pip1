a=input()
n=int(input())
N=[]
for i in range(0,n):
    N.append(input())
for i in range(0,3):
    for i in range(0,n):
        a.replace(N[i],'')
print(a)
