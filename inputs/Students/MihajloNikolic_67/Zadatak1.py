def saberi(lista):
    zbir = 0
    if(lista[-1] == '+'):
        zbir = int(lista[0]) + int(lista[1])
        print(str(zbir))

def oduzmi(lista):
    r = 0
    if(lista[-1] == '-'):
        r = int(lista[0]) - int(lista[1])
        print(str(r))

def mnozi(lista):
    p = 0
    if(lista[-1] == '*'):
        p = int(lista[0]) * int(lista[1])
        print(str(p))

def podeli(lista):
    d = 0
    if(lista[-1] == '/'):
        d = int(lista[0]) / int(lista[1])
        print(str(d))


    

lista = []
for i in range(3):
    lista.insert(i,input("Unesi prvi clan liste: "))

saberi(lista)
oduzmi(lista)
mnozi(lista)
podeli(lista)