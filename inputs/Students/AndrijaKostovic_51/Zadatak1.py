def sabiranje(x,y):
    rezultat=int(x)+int(y)
    return rezultat
def mnozenje(x,y):
    rezultat=int(x)*int(y)
    return rezultat
def oduzimanje(x,y):
    rezultat=int(x)-int(y)
    return rezultat
prvi_broj=input("Unesi prvi broj: ")
drugi_broj=input("Unesi drugi broj: ")
operacija=input("Unesite operaciju +,- ili *: ")

if(operacija == '+'):
    rezultat=sabiranje(prvi_broj,drugi_broj)
elif(operacija=='-'):
    rezultat=oduzimanje(prvi_broj,drugi_broj)
elif(operacija=='*'):
    rezultat=mnozenje(prvi_broj,drugi_broj)

print(str(rezultat))
    
