tekst=input()
n=tekst
reci=[]
for i in range(str(n)):
    rec=input()
    reci.append(rec)
while(True):
    brisanje=True
    for rec in reci:
        if(rec in tekst):
            brisanje=False
            tekst=tekst.replace(rec,"")

    if(brisanje):
        break
print(tekst)
