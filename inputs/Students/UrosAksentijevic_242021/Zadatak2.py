s = input()
n = int(input())
reci = []

for i in range(n):
    reci.append(input())

while True:
    flag = False
    for rec in reci:
        while rec in s:
            p = s.find(rec)
            if(p == -1):
                break
            s = s[ 0 : p ] + s[ p + len(rec) : ]
            flag = True
            
    if(flag == False):
        break

print(s)
