def Sabiranje (niz1,niz2):
    niz1=[]
    niz2=[]
    x=0
    y=0
    for i in range(0,len(niz1)):
        x=(x+niz1[i])*10
        if i==len(niz1)-1:
            x=x/10
    for i in range(0,len(niz2)):
        y=(y+niz2[i])*10
        if i==len(niz2)-1:
            y=y/10
    s=x+y
    return s

def Oduzimanje (niz1,niz2):
    niz1=[]
    niz2=[]
    x=0
    y=0
    for i in range(0,len(niz1)):
        x=(x+niz1[i])*10
        if i==len(niz1)-1:
            x=x/10
    for i in range(0,len(niz2)):
        y=(y+niz2[i])*10
        if i==len(niz2)-1:
            y=y/10
    s=x-y
    return s

def Mnozenje (niz1,niz2):
    niz1=[]
    niz2=[]
    x=0
    y=0
    for i in range(0,len(niz1)):
        x=(x+niz1[i])*10
        if i==len(niz1)-1:
            x=x/10
    for i in range(0,len(niz2)):
        y=(y+niz2[i])*10
        if i==len(niz2)-1:
            y=y/10
    s=x*y
    return s

a=input("Unesi prvi broj: ")
A=[]
for i in range(len(a)-1,0,-1):
    A.append(a[i])
b=input("Unesi drugi broj: ")
B=[]
for i in range(len(b)-1,0,-1):
    B.append(b[i])
c=input("Unesi znak racunske operacije: ")
if c=='+':
    rez=Sabiranje(A,B)
elif c=='-':
    rez=Oduzimanje(A,B)
elif c=='*':
    rez=Mnozenje(A,B)
R=[]
i=0
while rez/10>=0.1:
    R[i]=rez%10
    rez=(rez-R[i])/10
    i=i+1
R.reverse()
s=''
for i in range(0,len(R)):
    s[i]=R[i]
    s=s+s[i]
print(s)
