def brisi(rec,n,reci):
    for i in range(0,n):
        print(len(reci[i]))
        print(reci[i])
        print(rec[i:i+1])
        if(rec[0:len(reci[i])] != reci[i]):
            print(rec[i])

rec = input("Unesi rec: ")
n = int(input("Uneti broj reci za brisanje: "))

reci = []

for i in range(n):
    reci.insert(i,input("Uneti rec koja se izbacuje: "))

brisi(rec,n,reci)