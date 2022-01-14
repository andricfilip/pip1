def sabiranje(string1,string2):
    suma=string1+string2
    return suma
def oduzimanje(string1,string2):
    suma=string1-string2
    return suma
def mnozenje(string1,string2):
    suma=string1*string2
    return suma


string1=input()
string2=input()
operator=input()

if(operator=="+"):
    broj1=int(string1)
    broj2=int(string2)
    suma=sabiranje(broj1,broj2)
if(operator=="-"):
    broj1=int(string1)
    broj2=int(string2)
    suma=oduzimanje(broj1,broj2)
if(operator=="*"):
   broj1=int(string1)
   broj2=int(string2)
   suma=mnozenje(broj1,broj2)

rezultat=str(suma)
print(rezultat)

