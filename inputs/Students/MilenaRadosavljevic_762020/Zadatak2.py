s=input()

n=int(input())

lista=[]
for i in range(n):
    lista.insert(i, input())

novi=""
for i in range(len(s)):
    for j in range(n):
        if(lista[j]==s[i:i+len(lista[j])]):
            novi+=s[i+len(lista[j])]
print(novi)
