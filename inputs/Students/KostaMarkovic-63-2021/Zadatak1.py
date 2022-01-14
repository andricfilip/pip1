def Sabiranje(a,b):
    rez=int(a)+int(b)
    return rez

def Oduzimanje(a,b):
    rez=int(a)-int(b)
    return rez

def Mnozenje(a,b):
    rez=int(a)*int(b)
    return rez


a=input("")
b=input("")
c=input("")
if(c=='+'):
    rez=Sabiranje(a,b)
elif(c=='-'):
    rez=Oduzimanje(a,b)
else:
    rez=Mnozenje(a,b)

print(rez)
