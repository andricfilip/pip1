def sab(x,y):
    c=int(x)+int(y)
    return c
def odu(x,y):
    c=int(x)-int(y)
    return c
def mno(x,y):
    c=int(x)*int(y)
    return c
str=[]
x=input()
y=input()
z=input()
if(z=='+'):
    print(sab(x,y))
if(z=='-'):
    print(odu(x,y))
if(z=='*'):
    print(mno(x,y))

