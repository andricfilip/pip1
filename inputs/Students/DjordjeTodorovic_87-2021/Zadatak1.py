def Sabiranje(a,b):
    k=int(a)+int(b)
    print(str(k))
    
def Oduzimanje(a,b):
    k=int(a)-int(b)
    print(str(k))
    
def Mnozenje(a,b):
    k=int(a)*int(b)
    print(str(k))
    
def Izracunaj(a,b,zn):
    if (zn=="+"):
        Sabiranje(a,b)
    if (zn=="*"):
        Mnozenje(a,b)
    if (zn=="-"):
        Oduzimanje(a,b)


broj=input()
broj2=input()
znak=input()

Izracunaj(broj,broj2,znak)

