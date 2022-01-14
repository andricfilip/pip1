tekst = input()
N = int(input())
reci =[]

for i in range(N):
    reci.append(input())

while (True):
    iscrpi = True

    for rec in reci:
        if(rec in tekst):
            iscrpi = False
            tekst = tekst.replace(rec, "")

    if(iscrpi):
        break

print(tekst)

