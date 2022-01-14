def Postoji(string,niz):
    for i in range(len(niz)+1):
        c = str(niz[i])
        if(string.count(c) != 0):
            return 1
        else:
            return 0
    
rec = input()

n = int(input()) # broj reci koji se brise
niz_reci = []

for i in range(n):
    x = input()
    niz_reci = niz_reci + [x]

# koriscenjem replace sa praznim stringom
# x = str(niz_reci[0])
# print(rec.replace(x,""))

# x = str(niz_reci[0])
# rec = rec.replace(x,"")
# print(rec)

while(Postoji(rec,niz_reci)):
    for j in range(10):
        for i in range(n):
            p = str(niz_reci[i])
            rec = rec.replace(p,"")

print(rec)
