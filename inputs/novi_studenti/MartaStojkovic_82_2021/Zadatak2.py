rec = str(input(''))
br = int(input())
slog=[]
n=[]
for i in range(br):
    slog[i]=str(input(''))
for i in range(len(rec)):
    n[i] = rec.count(slog[i])
j=0
for i in range(n[j]):
    while(n[j]>0):
        rec=rec.del(s[i])
        n[j]=n[j]-1
    j = j+1
print(rec)

