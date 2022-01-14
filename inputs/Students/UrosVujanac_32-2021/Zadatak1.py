def Sabiranje(a,b):
    n=int(a)+int(b)
    return n

def Oduzimanje(a,b):
    n=int(a)-int(b)
    return n

def Mnozenje(a,b):
    n=int(a)*int(b)
    return n

a=input("Unesi prvi string: ")
b=input("Unesi drugi string: ")
znak=input("Operacije: ")

if(znak== "+"):
    print(Sabiranje(a,b))

elif(znak== "-"):
    print(Oduzimanje(a,b))

elif(znak== "*"):
    print(Mnozenje(a,b))
