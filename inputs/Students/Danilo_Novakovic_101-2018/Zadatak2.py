string=input()
n=int(input())
for i in range(n):
    nove=input()

lista=[]
lista=string.split()
for i in range(len(lista)):
    ind=False 
    if(i+1<len(lista)):
        j=i+1
        ind=True
        pom1=lista[i]+lista[j]
        pom=''.join(pom1)
        if((lista[i]!=lista[j])and pom==nove[j]):
            lista.pop(i)
            lista.pop(j)
    novi=''.join(lista)
    i=i+1
print(novi)
        

            
        
        
    




    
