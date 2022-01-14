a=input()
b=input()
oper=input()
na=len(a)
nb=len(b)
x=[]
y=[]
i=0
j=0
while(na>=0):
    x.insert(i,a[na-1])
    na-=1
    i+=1
while(nb>=0):
    y.insert(y,b[nb-1])
    nb-=1
    j+=1
    

print(int(x[0])+int(x[1]))
