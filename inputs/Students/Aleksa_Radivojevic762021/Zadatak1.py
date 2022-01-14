def sabiranje(lista):
    br=0
    for element in lista:
        br=br+1
    c=int(0)
    for i in range(br):
        c=c+int(lista[i])
    return c
def oduzimanje(lista):
    br=0
    for element in lista:
        br=br+1
    c=int(lista[0])
    for i in range(1,br):
        c=c-int(lista[i])
    return c
def mnozenje(lista):
    br=0
    for element in lista:
        br=br+1
    c=int(lista[0])
    for i in range(1,br):
        c=c*int(lista[i])
    return c
lista=[]
for i in range(2):
    lista.append(str(input()))
znak=str(input())
if(znak=='+'):
    c=sabiranje(lista)
elif(znak=='-'):
    c=oduzimanje(lista)
elif(znak=='*'):
    c=mnozenje(lista)
print(c)
            
