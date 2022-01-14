string1=input()
string2=input()
operacija=input()
if(operacija=='+'):
    m=len(string1)
    n=len(string2)
    a=[0]
    b=[0]
    rezultat=[]
    if(m>=n):
        br_cifara=m
        for i in range(m-n):
            b.append(0)
    elif(n>=m):
        br_cifara=n
        for i in range(n-m):
            a.append(0)
    for i in range(m):
        a.append(int(string1[i]))
    for i in range(n):
        b.append(int(string2[i]))
    for i in range(br_cifara+1):
        rezultat.append(0)
    prenos=0
    for i in range(br_cifara,-1,-1):
        if(a[i]+b[i]+prenos)<10:
            rezultat[i]=a[i]+b[i]+prenos
            prenos=0
        else:
            rezultat[i]=a[i]+b[i]+prenos-10
            prenos=1
    rezultat_string=''
    for i in range(len(rezultat)):
        if(i==0 and rezultat[i]==0):
            continue
        rezultat_string+=str(rezultat[i])
    print(rezultat_string)
elif(operacija=='-'):
    m=len(string1)
    n=len(string2)
    a=[0]
    b=[0]
    rezultat=[]
    if(m>=n):
        br_cifara=m
        for i in range(m-n):
            b.append(0)
    elif(n>m):
        br_cifara=n
        for i in range(n-m):
            a.append(0)
    for i in range(m):
        a.append(int(string1[i]))
    for i in range(n):
        b.append(int(string2[i]))
    for i in range(br_cifara+1):
        rezultat.append(0)
    for i in range(br_cifara,-1,-1):
        if(a[i]-b[i]>=0):
            rezultat[i]=a[i]-b[i]
        else:
            rezultat[i]=10+a[i]-b[i]
            a[i-1]=a[i-1]-1
    rezultat_string=''
    for i in range(len(rezultat)):
        if(i==0 and rezultat[i]==0):
            continue
        rezultat_string+=str(rezultat[i])
    print(rezultat_string)
            
        
