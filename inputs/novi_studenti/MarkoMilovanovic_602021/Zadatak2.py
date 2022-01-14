def Trazi(s,podniz):
    ima_podnizova = True
    while(ima_podnizova):
        ima_podnizova = False
        for i in range(len(podniz)):
            index = s.find(podniz[i])
            if index != (-1):
                s = s[:index] + s[(index + len(podniz[i])):]
                ima_podnizova = True
    return s


s = input()
n = int(input())
podniz = []
for i in range(n):
    podniz.append(input())
#print(podniz)
s = Trazi(s,podniz)
print(s)


    
        
