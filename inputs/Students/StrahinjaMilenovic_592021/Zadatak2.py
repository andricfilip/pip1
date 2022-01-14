mainstr = input()


n = int(input())
niz = ["" for i in range(n)]
for i in range (n):
    niz[i] = input()


for i in range (n):

        
    for j in range (n):
        while mainstr.find(niz[j]) > -1:
            mainstr = mainstr.replace(niz[j],"")
    if mainstr.find(niz[j]) > -1:
        i = 0

    
print(mainstr)
