def Sabiranje(a,b,k):
    i=len(a)
    n=len(b)
    m=0
    while (n>0):
        if(a[i-1]+k+m>10):
            a[i-1]=(a[i-1]+k+m)%10
            m=m+1
        else:
            a[i-1]=a[i-1]+k+m
            m=m-1
        n=n-1
        i=i-1
    return(a)
def Oduzimanje(a,b,k):
    i=len(a)
    n=len(b)
    m=10
    while (n>0):
        if(a[i-1]-k>0 or a[i-1]-k==0):
            a[i-1]=a[i-1]-k
            
        else:
            a[i-1]=a[i-1]-k+m
            a[i-2]=a[i-2]-1
        n=n-1
        i=i-1
    return(a)
def Deljenje(a,b,k):
    i=len(a)
    n=len(b)
    j=i
    m=1
    s1=0
    while (i>0):
        s1=s1+a[j-1]*m
        if(m==1):
            m=10
        else:
            m=m*10
        j=j-1
        i=i-1
    j=n
    m=1
    s2=0
    while (n>0):
        s2=s2+b[j-1]*m
        if(m==1):
            m=10
        else:
            m=m*10
        j=j-1
        n=n-1

    c=s1/s2
        
    return(c)
    

b=[]
a=[]
i=0
n=0
m=int(input(''))
p=m
while(p>0):
    p=p//10
    n=n+1
    


while(n>0):
    a.insert(i,m%10)
    m=int(m//10)
    i=i+1
    n=n-1
a.reverse()
i=0
n=0
k=int(input())
o=k
t=k
while(o>0):
    o=o//10
    n=n+1
    


while(n>0):
    b.insert(i,k%10)
    k=int(k//10)
    i=i+1
    n=n-1
b.reverse()
w=str(input(''))
if(w=='+'):
    print(Sabiranje(a,b,t))
elif(w=='-'):
    print(Oduzimanje(a,b,t))
elif(w=='/'):
    print(Deljenje(a,b,t))


