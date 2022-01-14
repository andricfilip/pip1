def Sabiranje(a,b):
    n = int(a) + int(b)
    return n

def Oduzimanje(a,b):
    n = int(a) - int(b)
    return n

def Mnozenje(a,b):
    n = int(a) * int(b)
    return n


a = input("Unesite prvi string: ")
b = input("Unesite drugi string: ")
znak = input("Operacija: ")

if(znak == "+"):
    print(Sabiranje(a,b))
elif(znak == "-"):
    print(Oduzimanje(a,b))
elif(znak == "*"):
    print(Mnozenje(a,b))
