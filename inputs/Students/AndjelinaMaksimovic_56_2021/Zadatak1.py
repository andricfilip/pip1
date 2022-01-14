def sabiranje(niz1,niz2,duzina1):
    rez_sab=[]
    pom_niz=[]
    rez=""
    for i in range(-1,-duzina1-1,-1):
        pom_niz=str(int(niz1[i])+int(niz2[i]))
        if(len(pom_niz)==2):
            rez_sab.insert(i,pom_niz[-1])
            niz1[i-1]=str(int(niz1[i-1])+int(pom_niz[-2]))
        else:
            rez_sab.insert(i,str(int(niz1[i])+int(niz2[i])))
            
    for i in range(len(rez_sab)):
        rez+=str(rez_sab[i])
    return(rez)

def oduzimanje(niz1,niz2,duzina1):
    rez_odu=[]
    rez=""
    for i in range(-1,-duzina1-1,-1):
        rez_odu.insert(i,str(int(niz1[i])-int(niz2[i])))
    for i in range(len(rez_odu)):
        rez+=str(rez_odu[i])
    return(rez)
        
unos1=str(input())
unos2=str(input())

niz1=[]
niz2=[]
rezultat=[]
for i in range(len(unos1)):
    niz1.append(unos1[i])

for i in range(len(unos2)):
    niz2.append(unos2[i])

duzina1=len(niz1)
duzina2=len(niz2)
j=duzina1-duzina2

for i in range(j):
    niz2.insert(i,0)


print("rezultat sabiranja",sabiranje(niz1,niz2,duzina1))


