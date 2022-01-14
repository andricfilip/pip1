string=input()
n = int(input())
A=[0 for i in range (n)]
novistring=[]
for i in range (n):
    x=input()
    A[i]=x
       
for i in range (n):
    string3 =string.replace(str(A[i]),'')

print(string3)







