string=input()
n=int(input())
niz=[]
for i in range(n):
    unesi=input()
    niz.append(unesi)
    
ind=1
br=0
i=0
resenje=""
while (niz[i]) in string:
    for j in range(len(string)):
        if(string[j]+string[j+1]==niz[i]):
            print(string[j])
            print(string[j+1])
            resenje+=string[j+2]+string[j+3]
            print(resenje)
        else:
            resenje+=string[j+1]+string[j+2]
            print(resenje)
    
    



