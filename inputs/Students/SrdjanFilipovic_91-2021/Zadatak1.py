def sabiranje(broj1,broj2,s3):
    rezultat=int(broj1.pop(0))+int(broj2.pop(0))
    return rezultat

def oduzimanje(broj1,broj2,s3):
    rezultat=int(broj1.pop(0))-int(broj2.pop(0))
    return rezultat

def mnozenje(broj1,broj2,s3):
    rezultat=int(broj1.pop(0))*int(broj2.pop(0))
    return rezultat

broj1=[]
broj2=[]

s1=input()
s2=input()
s3=input()

broj1=broj1+[s1]
broj2=broj2+[s2]

if(s3=="+"):
    rezultat=sabiranje(broj1,broj2,s3)
elif(s3=="-"):
    rezultat=oduzimanje(broj1,broj2,s3)
elif(s3=="*"):
    rezultat=mnozenje(broj1,broj2,s3)
    

print(rezultat)


    
