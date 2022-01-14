p=input("Unesi prvi string")
d=input("Unesi drugi string")
z=input("Unesi zna")
n1=len(p)
n2=len(d)
p1=[]
b=1
s=0
s1=0
c=0
r=0
for i in range(n1):
    p1.append(p[i])

for i in range(n1):
    c=pow(10,n1-b)
    s=s+c*int(p[i])
    b=b+1
b=1
for i in range(n2):
    c=pow(10,n2-b)
    s1=s1+c*int(d[i])
    b=b+1
print(s)
print(s1)
if(z=="+"):
    r=s+s1
if(z=="-"):
    r=s-s1
if(z=="*"):
    r=s*s1
if(z=="/"):
    r=s*s1
print(r)
    
    

    
