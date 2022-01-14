def Sabiranje(s1,s2,op):
    br1=int(s1)
    br2=int(s2)
    rez=br1+br2
    return str(rez)
def Oduzimanje(s1,s2,op):
    br1=int(s1)
    br2=int(s2)
    rez=br1-br2
    return str(rez)
def Mnozenje(s1,s2,op):
    br1=int(s1)
    br2=int(s2)
    rez=br1-br2
    return str(rez)



s1=input()
s2=input()
op=input()
resenje=''

if(op=='+'):
    resenje=Sabiranje(s1,s2,op)
    print(resenje)
elif(op=='-'):
    resenje=Oduzimanje(s1,s2,op)
    print(resenje)
elif(op=='*'):
    resenje=Mnozenje(s1,s2,op)
    print(resenje)
