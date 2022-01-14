rec = str(input("Unesi rec: "))
i = 0

n = int(input("Unesi broj reci: "))
lista_reci = []
for i in range(0,n):
    t = str(input())
    lista_reci.append(t)

duzina_reci = len(rec)
ind = True
i = 0
#print(duzina_reci)

for i in range(0,duzina_reci-1):
    for j in range(0,n):
        rec = rec.replace(lista_reci[j],'')
    
        
print(rec)
    
    
