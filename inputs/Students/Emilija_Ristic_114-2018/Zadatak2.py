print('Unesi rec\n')
rec = str(input())
print('Unesi broj reci\n')
n = int(input())
lista = []
i = 0
for i in range(0,n):
    temp = str(input())
    lista.append(temp)
print(lista)

for i in range(0,len(rec)):
    k = rec.find(lista[i])
    if(k != -1):
        rec.replace(rec[k],'')
        rec.replace(rec[k+1],'')
    
print(rec)


