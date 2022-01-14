print("Unesite pocetni tekst: ")
tekst = input()
n = int(input("Koliko reci trazite: "))

niz= []
for i in range(n):
    niz.append(i, int(input()))

for i in range(n):
    if(tekst[i] == niz[i]):
        tekst.pop(niz[i])