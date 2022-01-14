S=input()
n=int(input())
lista=[]
S1=[]
S1=S1+[S]
for i in range(n):
    lista.insert(i,input())

for i in range(len(S)):
    if(S.find(lista[i])!=0):
        S1.remove(lista[i])
print(S1)
        
    

