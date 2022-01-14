def sabiranje(niz1,niz2):
    n=len(niz1)
    m=len(niz2)
    i=n-1
    j=m-1
    novi=[]
    prenos=0
    k=0
    while(i>=0 or j>=0):
        if(prenos==0):
            broj=niz1[i]+niz2[j]
        else:
            broj=niz1[i]+niz2[j]+prenos
            prenos=0
        
        if(broj<10):
            novi.append(broj)
        else:
            prenos=1
            broj=broj-10
            novi.append(broj)
        i=i-1
        j=j-1
        if(i==-1 or j==-1):
            break
    d=len(novi)
    s=d
    i=n-1
    while(d>0):
        niz1.pop(i)
        i=i-1
        d=d-1
    j=s-1
    while(s>0):
        niz1.append(novi[j])
        j=j-1
        s=s-1
    return niz1
        
        
            


broj1=input()
broj2=input()
operacija=input()

niz1=[]
niz2=[]
rezultat=[]
n=len(broj1)
m=len(broj2)
for i in range(n):
    niz1.append(int(broj1[i]))

for i in range(m):
    niz2.append(int(broj2[i]))

if(operacija=="+"):
    rezultat=sabiranje(niz1,niz2)


pom=""
k=len(rezultat)
for i in range(k):
    pom=pom+str(rezultat[i])
print(pom)

