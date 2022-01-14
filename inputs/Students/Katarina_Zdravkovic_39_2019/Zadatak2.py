def prebaciUniz(rec):
    n=len(rec)
    niz=[]
    for i in range(n):
        niz.append(rec[i])
    return niz

def izbrisi(niz,c):
    n=len(niz)
    for i in range(n):
        if(niz[i]==c):
            niz=niz.remove(c)
            n=n-1
    return niz

def vratiUstring(niz):
    pom=""
    k=len(niz)
    for i in range(k):
        pom=pom+str(niz[i])
    return pom


rec=input()
duzina_reci=len(rec)
N=int(input())
niz=[]
for i in range(N):
    x=input()
    niz.append(x)

i=0
indikator=1

p=""
while(i<N):
    while(indikator==1):
            p=niz[i]
            broj=rec.count(p)
            rec.replace(p,"x",broj)
            duzina_reci=duzina_reci-broj
            rec=prebaciUniz(rec)
            rec=izbrisi(rec,"x")
            rec=vratiUstring(rec)
            duzina_reci=len(rec)
            provera=rec.count(p)
            
            if(provera==0):
                indikator=0
    i=i+1
    indikator==1
    if(i==N):
        break

print(rec)

