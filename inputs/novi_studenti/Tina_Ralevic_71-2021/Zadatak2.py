rec = input()
m = len(rec)


n = int(input())
print(rec)
for i in range(n):
    podrec = input()
    indeks = rec.find(podrec)
    print(indeks)
    rec = list(rec)
    print(rec)
    del(rec[indeks:(indeks+len(podrec)])
    rec = "".join(rec)
print (rec)

