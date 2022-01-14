a=input("Unesi pocetnu rec: ")
n=int(input("Broj reci koji se izbacuje: "))
p=""
for i in range(n):
    b=input()
for i in range(len(a)-1):
    if(a[i]==b):
       a.replace(a[i],str(p))
print(a)
