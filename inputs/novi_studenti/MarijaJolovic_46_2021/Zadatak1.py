def sabiranje(s1,s2):
    s=""
    d1 = len(s1)
    d2 = len(s2)
    if d1<d2:
        d1,d2=d2,d1
        s1,s2=s2,s1
    for i in range(d1-d2):
            s+=s1[i]
    prenos = 0
    i=d1-1
    j=d2-1
    out=""
    while(i>d1-d2-1 and j>=0):
        #print(s1[i],s2[j])
        zbir = int(s1[i])+int(s2[j])+prenos
        out+=str((zbir)%10)
        if ((zbir)>=10):
            prenos=1
        else:
            prenos=0
        #print(zbir,prenos)
        j=j-1
        i=i-1
    out=list(out)
    out.reverse()
    for i in out:
        s+=i
    #print(s)
    if (prenos and d1==d2):
        s=str(prenos)+s
    elif (prenos):
        clan = int(s[d1-d2-1])
        clan+=prenos
        #print(clan)
        s=s.replace(s[d1-d2-1],str(clan),1)
    return s

def mnozenje(s1,s2):
    s=""
    stepen=1
    d1 = len(s1)
    d2 = len(s2)
    prenos=0
    p0="0"
    for j in range(d2-1,-1,-1):
        p=""
        prenos=0
        for i in range(d1-1,-1,-1):

            clan = int(s1[i])*int(s2[j])
            if prenos:
                clan+=prenos
            if clan>=10:
                prenos=clan//10
            else :
                prenos=0
            p+=str(clan%10)
            #print(p)
        if prenos:
            p=p+str(prenos)
        
        p=list(p)
        p.reverse()
        p1=""
        for i in p:
            p1+=str(i)
        for i in range(stepen-1):
            p1+="0"
        #print(p0,p1)
        s=sabiranje(p0,p1)
        p0=s
        stepen=stepen+1
        #print(s)
    return s

def oduzimanje(s1,s2):
    s=""
    if s1<s2:
        s1,s2=s2,s1
    return s

s1 = input("")
s2 = input("")
oper = input("")

s=""
if oper=="+":
    s=sabiranje(s1,s2)
elif oper=="*":
    s=mnozenje(s1,s2)
elif oper=="-":
    s= oduzimanje(s1,s2)

print(s)