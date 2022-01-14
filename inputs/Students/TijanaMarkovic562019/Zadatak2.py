string=str(input())
n1=int(input())
niz=[]
for i in range(n1):
    x=input()
    niz.append(x)
i=0
n=len(string)
niz_duzina=[]
for i in range(n1):
    duz=len(niz[i])
    niz_duzina.append(duz)
print(niz_duzina)
while(i<n1):
    j=0
    while(j<n):
        duzina=j+niz_duzina[i]
        if(string[j:duzina]==niz[i]):
            p=j
            l=duzina-j
            c=0
            while(p<n):
                string[p]=string[duzina+c]
                c=c+1
                n=n-l
                p=p+1
        else:
            j=j+1

    i=i+1
print(string)
