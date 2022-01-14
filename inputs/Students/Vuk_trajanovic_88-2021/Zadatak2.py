a=input("rec je ")


n=int(input("izbacuje se ovoliko reci: "))

reci=[]
for i in range(n):
    rec=input("rec za brisanje je ")
    reci.append(rec)
    
print(reci)
j=0
krug=a
krug1=a+"  "
while krug1!=krug:
    for i in range(n):
        while(a.i!=-1):
            a=a.replace(rec[i:i+2],"")
            print(a,rec[i:i+2])



print(a)
