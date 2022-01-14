string = input("")

n = int(input(""))
kar=[0 for i in range(n)]
for i in range(n):
    clan=input()
    kar[i]=str(clan)
i=0
rec= string
nova_rec = rec.replace(kar[i],"")
while (rec!=nova_rec):
    rec=nova_rec
    i+=1
    if i==n:
        i=0
    nova_rec = rec.replace(kar[i],"")
print(nova_rec)