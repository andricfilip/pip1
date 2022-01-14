def saberi(an,bn,a,b):
    niz = []
    prenos = 0
    duzina = max(an,bn)
    i = 1
    while i<=duzina:
        if(i<=an and i<=bn):
            niz.insert(0,(a[an-i]+b[bn-i]+prenos))
        elif(i>an and i<=bn):
            niz.insert(0,(b[bn-i]+prenos))
        elif (i>bn and i<=an):
            niz.insert(0,(a[an-i]+prenos))

        temp = int(niz[0])

        prenos = temp//10
        niz[0] = str(temp%10)
        print(niz)
        print(niz[0])

        
        i+=1
    if(prenos == 1):
        niz.insert(0,prenos)
    return niz

def oduzmi(a,b):
    for i in range(len(a)):
        a[i] = str(a[i])
    for i in range(len(b)):
        b[i] = str(b[i])
    c = int("".join(a)) - int("".join(b))
    return c
# poeni na poznavanju python-a
def mnozi(a,b):
    for i in range(len(a)):
        a[i] = str(a[i])
    for i in range(len(b)):
        b[i] = str(b[i])
    c = int("".join(a)) * int("".join(b))
    return c



def main():

    a = list(input())
    b= list(input())
    an = len(a)
    bn = len(b)
    for i in range(an):
        a[i] = int(a[i])
    
    for i in range(bn):
        b[i] = int(b[i])

    operacija = (input())[0]

    if (operacija == "+"):
        c = saberi(an,bn,a,b)
    elif (operacija == "-"):
        c = oduzmi(a,b)
    elif (operacija == "*"):
        c = mnozi(a,b)
    print(c)

main()

