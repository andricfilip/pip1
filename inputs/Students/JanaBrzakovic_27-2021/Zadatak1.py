broj1=str(input('prvi broj: '))
broj2=str(input('drugi broj: '))
op=str(input('operator: '))
duzi=[]
kraci=[]
sabiranje=False
oduzimanje=False
if(len(broj1)>len(broj2)):
    kracistr=broj2
    duzistr=broj1
    for i in range(len(broj1)):
        duzi.append(broj1[i])

    for i in range(len(broj2)):
        kraci.append(broj2[i])
else:
    kracistr=broj1
    duzistr=broj2
    for i in range(len(broj2)):
        duzi.append(broj2[i])

    for i in range(len(broj1)):
        kraci.append(broj1[i])    

if(kraci[0]=='-' and duzi[0]=='-'):
    sabiranje=True
elif(kraci[0]=='-' and duzi[0]!='-') or (kraci[0]!='-' and duzi[0]=='-'):
    oduzimanje=True
elif(kraci[0]!='-' and duzi[0]!='-'):
    sabiranje=True

sabirak1=[]
zbir=''
if(sabiranje):
    for i in range(len(kraci)+1):
        sabirak1.append(duzi[-1-i])
        if(i==len(kraci)):
            pocetna_pozicija=i
    sabirak1.reverse()
    string=''
    for i in range(len(sabirak1)):
        string+=sabirak1[i]
    zbir=int(string)+abs(int(kracistr))
    for i in range(len(duzi)-1,i-1,-1):
        duzi.pop(i)
    for i in range(len(string)):
        duzi.append(string[i])
print(duzi)
