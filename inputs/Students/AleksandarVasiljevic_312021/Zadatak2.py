n=str(input(''))
k=int(input())
a=['']
i=0
j=0
w=[[n]]
p=n.find(a[j])
while(k>0):
    x=str(input(''))
    a[i]=x
    i=i+1
    k=k-1


while(i>0):
    
    if(p!=-1):
        o=len(a[j])
        while(o>0):
            w.pop(p)
            o=o-1

    i=i-1
    j=j+1



print(w)
