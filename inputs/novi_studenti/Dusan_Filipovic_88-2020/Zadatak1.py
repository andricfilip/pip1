prvi_sabirak=input()
drugi_sabirak=input()
operand=input()

duzinaPrvog=len(prvi_sabirak)
duzinaDrugog=len(drugi_sabirak)
print(duzinaPrvog)
print(duzinaDrugog)
pocetakDrugog=0
uzimam=[]
resenje=[]
if(duzinaPrvog>duzinaDrugog):
    potpis=duzinaDrugog
    for i in range(0,duzinaDrugog):
        uzimam.append((prvi_sabirak[i+duzinaPrvog-duzinaDrugog]))
    for i in range(0,duzinaPrvog-duzinaDrugog):
        resenje.append(prvi_sabirak[i])
    saberi=0
    stepen=1
    broj=0
    pamtim=0
    for i in range(len(uzimam)):
        if(operand=='+'):
            cifra=pamtim+int(uzimam[len(uzimam)-1-i])+int(drugi_sabirak[len(uzimam)-1-i])
            if(cifra>9):
                pamtim=cifra-10
            broj+=cifra*stepen
            cuvar=stepen
            stepen*=10
        print(broj)
   
    resenje+=str(broj)
    print(resenje)

