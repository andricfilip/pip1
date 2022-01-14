def sabiranje(a,b):
    d=a+b
    return d
def oduzimanje(a,b):
    d=a-b
    return d
def mnozenje(a,b):
    d=a*b
    return d
a=int(input("Unesi string1: "))
b=int(input("Unesi string2: "))
c=input("Unesi string3: ")
if(c=="+"):
  print(sabiranje(a,b))
elif(c=="-"):
    print(oduzimanje(a,b))
elif(c=="*"):
    print(mnozenje(a,b))

    
    

