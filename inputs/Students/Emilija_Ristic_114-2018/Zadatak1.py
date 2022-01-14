def saberi(lista_prva,lista_druga,duzina1, duzina2):
    while(duzina2 > 0):
        duzina1 = duzina1-1
        duzina2 = duzina2-1
        if(lista_prva[duzina1]+lista_druga[duzina2] > 10):
            prenos = lista_prva[duzina1]+lista_druga[duzina2]
            prenos = prenos % 10
            lista_prva[duzina1] = lista_prva[duzina1]+lista_druga[duzina2]
            lista_prva[duzina1-1] = lista_prva[duzina1-1] + prenos
        else:
            lista_prva[duzina1] = lista_prva[duzina1]+lista_druga[duzina2]
        
    print(str(lista_prva))
    
def mnozi(lista_prva,lista_druga,duzina1,duzina2):
    duzina1 = duzina1-1
    duzina2 = duzina2-1
    i = duzina1-1
    while(duzina2>0):
        duzina1 = i
        while(duzina1 > 0):
            lista_prva[duzina1] = lista_prva[duzina1]*lista_druga[duzina2]
            duzina1 = duzina1-1
        duzina2 = duzina2-1
    print(str(lista_prva))
    
def oduzmi(lista_prva,lista_druga,duzina1, duzina2):
    duzina1 = duzina1-1
    duzina2 = duzina2-1
    while(duzina2 > 0):
        if(lista_prva[duzina1]-lista_druga[duzina2] < 10):
            prenos = lista_prva[duzina1]-lista_druga[duzina2]
            prenos = prenos % 10
            lista_prva[duzina1] = lista_prva[duzina1]-lista_druga[duzina2]
            lista_prva[duzina1+1] = lista_prva[duzina1+1] - prenos
        else:
            lista_prva[duzina1] = lista_prva[duzina1]-lista_druga[duzina2]
        
    print(str(lista_prva)) 


lista_prva = []
lista_druga = []


unos1 = str(input())
print(unos1)
unos2 = str(input())
print(unos2)
operacija = str(input())
print(operacija)

duzina1 = len(unos1)

duzina2 = len(unos2)
#print('duzina2 ',duzina2)

for i in range(0,duzina1):
    temp = int(unos1[i])
    lista_prva.append(temp)
    
for j in range(0,duzina2):
    temp = int(unos2[j])
    lista_druga.append(temp)


if(operacija == '+'):
    print('Potrebno je sabiranje')
    saberi(lista_prva,lista_druga,duzina1,duzina2)
    
elif(operacija == '-'):
    print('Potrebno je oduzimanje')
    oduzmi(lista_prva,lista_druga,duzina1,duzina2)

elif(operacija == '*'):
    print('Potrebno je mnozenje')
    mnozi(lista_prva,lista_druga,duzina1,duzina2)

else:
    print('Operacija je nepoznata')
    
