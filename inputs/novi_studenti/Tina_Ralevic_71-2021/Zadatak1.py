string1 = input() #broj
string2 = input() #broj
operacija = input()

lista1 = list(string1)
print(lista1)
lista2 = list(string2)
n = len(lista1)
m = len(lista2)
for i in range(0, n-m):
    lista2.insert(i, 0)
print(lista2)
    
def izracunavanje(a,b):
    if(operacija == "+"):
        s = a+b
    elif(operacija == "-"):
        s = a-b
    elif(operacija == "*"):
        s = a*b
    s = str(s)
    return s

   
i = n-1
while(i!=(-1)):
    s = 0
    a = int(lista1[i])
    b = int(lista2[i])
    if (s>9):
        a +=1
    s = izracunavanje(a,b)
    lista1[i] = s
    i-=1
lista1 = "".join(lista1)
print(lista1)
    
        
    
    
    
