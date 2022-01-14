prvi = input("Unesite prvi broj: ")
drugi = input("Unesite drugi broj: ")
znak = input("Unesite znak: ")
suma = 0
nizsume = []
nizraz = []
niz = []
niz2 = []

prviLen = len(prvi)
drugiLen = len(drugi)

maxx = max(prviLen, drugiLen)
minn = min(prviLen, drugiLen)

razlika = maxx-minn

for i in range(prviLen):
    niz = niz + [prvi[i]]
      
for i in range(drugiLen):
    niz2 = niz2 + [drugi[i]]





if znak == '+':
    for i in range (minn):
        suma=0
        suma = suma + int(niz[maxx-i-1]) + int(niz2[maxx-razlika-i-1])
        nizsume = nizsume + [suma]
    nizsume.reverse()
    novistr = prvi[:-4] + str(nizsume)
    print(novistr)









