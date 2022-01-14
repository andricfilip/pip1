string=input()
n=int(input("Unesi broj reci: "))
reci=[]
for i in range(n):
    reci.append(input())
while(True):
    da_li_je_iscrpljeno=True
    for rec in reci:
        if(rec in string):
            da_li_je_iscrpljeno=False
            string=string.replace(rec,"")
    if(da_li_je_iscrpljeno):
        break
print(string)
