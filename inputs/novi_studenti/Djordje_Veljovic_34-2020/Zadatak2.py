rec=input()
n=int(input())
niz=[]
for i in range(n):
    t=input()
    niz.append(t)

d=len(rec)
for i in range(len(niz)):
    j=0
    while(j<d-1):
        if(rec[j:j+2]==niz[i]):
            rec=rec[0:j]+rec[j+2:len(rec)]
        j=j+1
for i in range(len(niz)):
    j=0
    while(j<d-1):
        if(rec[j:j+2]==niz[i]):
            rec=rec[0:j]+rec[j+2:len(rec)]
        j=j+1
    
print(rec)
