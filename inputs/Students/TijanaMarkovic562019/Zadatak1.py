def sabiranje(broj1,broj2):
    return broj1+broj2
def oduzimanje(broj1,broj2):
    return broj2-broj1
def mnozenje(broj1,broj2):
    return broj1*broj2

prvi=str(input())
drugi=str(input())
operacija=str(input())
niz1=[]
niz2=[]
n1=len(prvi)
n2=len(drugi)
for i in range(n1):
    broj1=prvi[i]
    broj1=int(broj1)
    niz1.append(broj1)
for j in range(n2):
    broj2=drugi[j]
    broj2=int(broj2)
    niz2.append(broj2)
p=1
prvi_broj=0
drugi_broj=0
print(niz1)
print(niz2)
for i in range(n1-1,-1,-1):
    prvi_broj=prvi_broj+niz1[i]*p
    p=p*10
p=1
for j in range(n2-1,-1,-1):
    drugi_broj=drugi_broj+niz2[j]*p
    p=p*10
if (operacija=="+"):
    uk=sabiranje(prvi_broj,drugi_broj)
if(operacija=="-"):
    uk=oduzimanje(prvi_broj,drugi_broj)
if(operacija=="*"):
    uk=mnozenje(prvi_broj,drugi_broj)

string=str(uk)
print(string)
