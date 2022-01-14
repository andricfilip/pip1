s=input()
a=input()
znak=input()
a1=int(a)
plus="+"
minus="-"
puta="*"
pom=a1
br=0
while(pom!=0):
    br=br+1
    pom=pom//10

print(br)    

if (znak==plus):
    pom1=0
    for i in range (1,br+1):
        #x=int(s[-i])
        #print(x)
        zbir=int(s[-i])+(a1%10)+pom1
        if (zbir>9):
            p=str(zbir%10)
            t=s[-i]
            s.replace(t,p,1)
            print("string",s)
            pom1=zbir//10
            print("pom1:", pom1)
        else:
            t=s[-i]
            s.replace(t,str(zbir),1)
        a1=a1//10


elif (znak==minus):
    for i in range (1,br+1):
        if ((a1%10)>int(s[-i]):
            x=int(s[-i])+10-a1%10
            a=int(s[-i-1])-10
            t=s[-i]
            p=str(x)
            s.replace(t,p,1)
        else:
            x=int(s[-i])-a1%10
            t=s[-i]
            p=str(x)
            s.replace(t,p,1)
        a1=a1//10

else:
    pom1=1
    for i in range (1,br+1):
            x=int(s[-i])*a1%10*pom1
            pom1=x//10
            t=s[-i]
            p=str(x%10)
            s.replace(t,p,1)
            a1=a1//10

print(s)
