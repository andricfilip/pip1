rec = input()
n = int(input())

p = []

for i in range(n):
    p.append(input())

i=0
while (True):
    rec1=rec
    rec1 = rec1.replace(p[i%n], "")
    if(rec1==rec):
        break
    rec = rec1
    i+=1

print(rec)