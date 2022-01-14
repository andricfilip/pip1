#def Sabiranje(jedan,dva):
#    p = len(jedan)
#    q = len(dva)
#    for i in range


x = input()
y = input()
z = input() # +, -, *

listaX = []
listaY = []

for i in range(len(x)):
    pom1 = x[i]
    listaX = listaX + [pom1]

for i in range(len(y)):
    pom2 = y[i]
    listaY = listaY + [pom2]

resenje = Sabiranje(listaX,listaY)
print(resenje)
