def sabiranje(str1,str2):
    d2=len(str2)
    d1=len(str1)
    nov=[0 for j in range(d2)]
    for i in range(d2):
        a=int(string1[-i-1])
        b=int(string2[-i-1])
        print(a,b)
        nov[i]=a+b+p
        if(a+b>=10):
            nov[i]=a+b-10
            p=1
        else:
            p=0
    for i in range(d2):
        str1[-i-1]=nov[i]
    print(str1)
        
string1=input("unesi 1. string")
string2=input("unesi 2.string")
string3=input("unesi operaciju")

if (string3=='+'):
    sabiranje(string1,string2)
