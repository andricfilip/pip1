rec=input()

n=int(input("broj reci koje se izbacuju"))
niz=[]

for i in range(n):
    rec2=input()
    niz.append(rec2)
print(niz)

for i in range(len(rec)):
    for i in range(n):
        rec=rec.replace(niz[i],"")
   
    
print(rec)



