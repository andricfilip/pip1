def IzbaciNiz(A,M):
    for i in range(len(M)):
        if(A[i]+A[i+1]==m):
            rez= A.Remove(m)
            return rez
rec=input("")
n=int(input(""))
for i in range(n):
    m=input("")

for j in range(len(rec)):
        rec=IzbaciNiz(rec,m)
        pom=rec
        if(pom==rec):
            break

print(rec)
    
    
