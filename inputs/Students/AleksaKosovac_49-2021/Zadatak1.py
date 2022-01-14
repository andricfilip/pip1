lista=[]
lista1=[]
lista2=[]
listapom=[]
lista1pom=[]
listakraj=[]

n=int(input("Unesi prvi broj: "))
m=int(input("Unesi drugi broj: "))
p=input("Unesi operaciju: ")

j=n
l=m

k=n%10
lista=[k]
n//=10

while(n>0):
    k=n%10
    lista.append(k)
    n//=10
#lista.reverse()
#print(lista)

while(m>0):
    g=m%10
    lista1.append(g)
    m//=10
#lista1.reverse()
#print(lista1)

if(len(lista)>len(lista1)):
    lista=lista
    lista1=lista1
else:
    t=lista
    lista=lista1
    lista1=t

pom1=len(lista)
pom=len(lista1)


'''
1 7 3 5 9

3 2 4

45

13

585
'''
br=0
if(p=='+'):
    for i in range(pom,pom1):
        k=0
        lista1.append(k)
    for i in range(0,pom1):
        d=lista[i]+lista1[i]
        if(d<10):
            rez=d+br
            listakraj.append(rez)
            br=0
        else:
            d=d-10
            br=1
            listakraj.append(d)
    listakraj.reverse()
    for i in listakraj:
        print(i,end='')
elif(p=='-'):
    for i in range(pom,pom1):
        k=0
        lista1.append(k)
    for i in range(0,pom1):
        d=lista[i]-lista1[i]
        if(d<0):
            b=-d
            listakraj.append(b)
            br=-1
        else:
            rez=d+br
            listakraj.append(rez)
            br=0
    listakraj.reverse()
    for i in listakraj:
        print(i,end='')
elif(p=='*'):
    '''
    for i in range(pom,pom1):
        k=1
        lista1.append(k)
        print(lista1)
    '''
    e=j*l
    print(e)

