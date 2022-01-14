prvi=input()
drugi=input()
lista1=[]
lista2=[]
prvi1=int(prvi)
drugi2=int(drugi)
while prvi1!=0:
    c1=c%10
    c=str(c1)
    lista1.append(c)
    lista1.reverse()
    prvi1=prvi1//10
while drugi1!=0:
    c1=c%10
    c=str(c1)
    lista2.append(c)
    list2.reverse()
    drugi2=drugi2//10
    
if(operacija=='+'):
    novi=''.join(lista1)
    novi1=''.join(lista2)
    novi2=int(novi)
    novi3=int(novi)
    s=novi2+novi3
    s1=str(s)
    print(s1)
    
elif(operacija=='-'):
     novi=''.join(lista1)
     novi1=''.join(lista2)
     novi2=int(novi)
     novi3=int(novi)
     s=novi2-novi3
     s1=str(s)
     print(s1)
        
         
     
elif(operacija=='*'):
     novi=''.join(lista1)
     novi1=''.join(lista2)
     novi2=int(novi)
     novi3=int(novi)
     s=novi2*novi3
     s1=str(s)
     print(s1)
     
elif(operacija=='/'):
    novi=''.join(lista1)
    novi1=''.join(lista2)
    novi2=int(novi)
    novi3=int(novi)
    s=novi2/novi3
    s1=str(s)
    print(s1)
    
    
    
    
    
