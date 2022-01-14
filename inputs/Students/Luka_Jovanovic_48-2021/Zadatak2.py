tekst=input()
N=tekst()
reci=[]

for i in range(N):
    rec=input()
    reci.append(rec)

while(True):
    iscrpljeno=True

    for rec in reci:
        if(rec in tekst):
            iscrpljeno=False
            tekst=tekst.replace(rec,"")
            
      

    if(iscrpljeno):
        break
      
    

print(tekst)

    

 
    

      
       
       
