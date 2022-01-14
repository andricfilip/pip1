a=input("broj 1 je ")
b=input("broj 2 je ")
c=input("operacija je ")
broj2=int(b)
duz=len(a)
dec=0
while broj2!=0:
    dec=dec+1
    broj2=broj2//10
broj2=int(b)

if c=="+":
    broj1=int(a[duz-dec:duz])
    nov=broj1+broj2
    dec1=0
    nov1=nov
    while nov1!=0:
        dec1=dec1+1
        nov1=nov1//10
    if dec==dec1:
        
        rez=a[0:duz-dec]+str(nov)
    else:
        rez=a[0:duz-dec1]+str(nov+int(a[duz-dec1])*((10**dec1)//10))

if c=="-":
    broj1=int(a[duz-dec:duz])
    nov=broj1-broj2

    if nov>=0:
        
        rez=a[0:duz-dec]+str(nov)
    else:
        rez=a[0:duz-dec-1]+str(     nov+int(a[duz-dec-1])*(10**(dec))    )
if c=="*":
    rez=int(a)*int(b)
    
        
print(rez)
